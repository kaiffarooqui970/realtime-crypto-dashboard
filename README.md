<div align="center">

# 📊 Real-Time Cryptocurrency Dashboard

**A production-ready streaming data pipeline with live visualizations**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[Live Demo](https://your-demo-link.streamlit.app) • [Report Bug](https://github.com/yourusername/realtime-crypto-dashboard/issues) • [Request Feature](https://github.com/yourusername/realtime-crypto-dashboard/issues)

<img src="assets/dashboard-preview.gif" alt="Dashboard Preview" width="800"/>

</div>

---

## 🎯 Overview

This project demonstrates **end-to-end data engineering** skills by building a real-time streaming dashboard that:

- 📡 **Streams live data** from Binance WebSocket API
- 💾 **Persists data** in a SQLite database with thread-safe operations
- 📈 **Visualizes trends** with interactive Plotly charts
- 🐳 **Deploys anywhere** via Docker containerization

> Built as a portfolio project to showcase real-world data engineering, Python development, and MLOps-adjacent skills.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔴 Real-Time Streaming
- WebSocket connection to Binance API
- Automatic reconnection on failure
- REST API fallback mechanism
- Configurable polling intervals

</td>
<td width="50%">

### 📊 Interactive Visualizations
- Live price charts with Plotly
- Normalized comparison view
- Price change metrics
- Customizable time ranges

</td>
</tr>
<tr>
<td width="50%">

### 🗄️ Robust Data Layer
- Thread-safe SQLite operations
- Indexed queries for performance
- Automatic data cleanup
- Easy migration to PostgreSQL

</td>
<td width="50%">

### 🚀 Production Ready
- Dockerized deployment
- Health check endpoints
- Comprehensive test suite
- Clean, modular architecture

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.11+ |
| **Frontend** | Streamlit, Plotly |
| **Data Streaming** | WebSocket, REST API |
| **Database** | SQLite (PostgreSQL ready) |
| **DevOps** | Docker, GitHub Actions |
| **Testing** | pytest |

---


---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip or conda
- Docker (optional)

### Option 1: Local Development

```bash
# Clone the repository
git clone [github.com](https://github.com/yourusername/realtime-crypto-dashboard.git)
cd realtime-crypto-dashboard

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run src/dashboard.py
# Build the image
docker build -t crypto-dashboard .

# Run the container
docker run -p 8501:8501 crypto-dashboard
[localhost](http://localhost:8501)
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
