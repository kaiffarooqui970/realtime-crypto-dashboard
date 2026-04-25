import json
import websocket
from database import CryptoDatabase

# Connect to Binance's public stream for BTC, ETH, and SOL trades
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade/ethusdt@trade/solusdt@trade"

# Initialize our database connection
db = CryptoDatabase()

def on_message(ws, message):
    """Triggered every time a new price update comes in."""
    data = json.loads(message)
    
    # Binance payload uses 's' for symbol, 'p' for price, and 'q' for volume
    if 's' in data and 'p' in data:
        symbol = data['s']
        price = float(data['p'])
        volume = float(data['q'])
        
        # Save it directly to our SQLite database
        db.insert_price(symbol, price, volume)
        print(f"Saved -> {symbol}: ${price:,.2f} (Vol: {volume})")

def on_error(ws, error):
    print(f"WebSocket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket Connection Closed. Attempting to reconnect...")

def on_open(ws):
    print("Successfully connected to Binance WebSocket!")
    print("Listening for live BTC, ETH, and SOL prices...")

if __name__ == "__main__":
    # Set up and run the websocket connection
    ws = websocket.WebSocketApp(
        BINANCE_WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    
    # Keep the connection alive
    ws.run_forever(ping_interval=60, ping_timeout=10)