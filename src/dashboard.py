import streamlit as st
import pandas as pd
import plotly.express as px
import time
from database import CryptoDatabase

# Configure the Streamlit page
st.set_page_config(page_title="Real-Time Crypto Dashboard", layout="wide")
st.title("🚀 Real-Time Crypto Price Dashboard")

# Connect to our database
db = CryptoDatabase()

# Fetch the most recent prices to display at the top
latest_prices = db.get_latest_prices()

if not latest_prices:
    st.warning("Waiting for data... Make sure your data_streamer.py is running in the other terminal!")
    st.stop()

# Create dynamic metric cards
cols = st.columns(len(latest_prices))
for i, (symbol, price) in enumerate(latest_prices.items()):
    with cols[i]:
        st.metric(label=symbol, value=f"${price:,.2f}")

st.markdown("---")

# Let the user pick which coin to look at on the chart
selected_symbol = st.selectbox("Select Crypto to View Chart", list(latest_prices.keys()))

# Fetch the last 100 price points for the selected coin
recent_data = db.get_recent_prices(selected_symbol, limit=100)

if recent_data:
    # Convert our database rows into a Pandas DataFrame for easy charting
    df = pd.DataFrame(recent_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Draw the line chart using Plotly
    fig = px.line(
        df, 
        x='timestamp', 
        y='price', 
        title=f"Live {selected_symbol} Price", 
        markers=True
    )
    fig.update_layout(xaxis_title="Time", yaxis_title="Price (USD)")
    
    # Display it on the screen
    st.plotly_chart(fig, use_container_width=True)

# Force the Streamlit app to refresh every 2 seconds so the chart animates
time.sleep(2)
st.rerun()