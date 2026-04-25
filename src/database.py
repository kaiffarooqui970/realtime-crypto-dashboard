import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
import threading

class CryptoDatabase:
    """Thread-safe SQLite database for storing crypto prices."""
    
    def __init__(self, db_path: str = "crypto_prices.db"):
        self.db_path = db_path
        self.lock = threading.Lock()
        self._init_db()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Create a new connection for the current thread."""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _init_db(self) -> None:
        """Initialize the database schema."""
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    price REAL NOT NULL,
                    volume REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_symbol_timestamp 
                ON prices(symbol, timestamp)
            """)
            conn.commit()
            conn.close()
    
    def insert_price(self, symbol: str, price: float, volume: float = None) -> None:
        """Insert a new price record."""
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO prices (symbol, price, volume) VALUES (?, ?, ?)",
                (symbol, price, volume)
            )
            conn.commit()
            conn.close()
    
    def get_recent_prices(
        self, 
        symbol: str, 
        limit: int = 100
    ) -> List[Dict]:
        """Get recent prices for a symbol."""
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT symbol, price, volume, timestamp 
                FROM prices 
                WHERE symbol = ? 
                ORDER BY timestamp DESC 
                LIMIT ?
            """, (symbol, limit))
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows][::-1]  # Reverse for chronological order
    
    def get_latest_prices(self) -> Dict[str, float]:
        """Get the latest price for each symbol."""
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT symbol, price, MAX(timestamp) as timestamp
                FROM prices 
                GROUP BY symbol
            """)
            rows = cursor.fetchall()
            conn.close()
            return {row['symbol']: row['price'] for row in rows}
    
    def cleanup_old_data(self, hours: int = 24) -> int:
        """Delete data older than specified hours."""
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM prices 
                WHERE timestamp < datetime('now', ?)
            """, (f'-{hours} hours',))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()
            return deleted