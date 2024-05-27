# Trading Dashboard

This project is a trading dashboard using Dhan API. It includes functionalities to fetch current holdings, place buy and sell orders, get postback updates from the broker, and receive live prices through a WebSocket.

## Features

1. **Fetch Current Holdings**: Retrieve the list of current holdings in your account.
2. **Place Orders**: Ability to place buy and sell orders with various parameters.
3. **Postback**: Receive updates on the status of orders (e.g., pending, rejected, traded).
4. **Live Feed**: Get live updates of Last Traded Price (LTP) from the broker's WebSocket.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pandas
- WebSocket library
- DhanHQ Python SDK
- dotenv

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Dang3Rsm/TradeDhasboardProj0
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Dhan client ID and access token:
    ```env
    FLASK_SECRET_KEY=flask_secret_key
    CLIENT_ID=your_client_id
    ACCESS_TOKEN=your_access_token
    POSTBACK_URL=http://your-postback-url.com
    ```

### Usage

1. **Run the Flask application**:
    ```bash
    python flaskApp.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to access the web interface.

### API Endpoints

- **/holdings**: View current holdings.
- **/place_order**: Place a new order (buy or sell).
- **/live_feed**: View live feed of Last Traded Prices (LTP).

### Directory Structure
```
├── templates/
│ ├── layout.html
│ ├── holdings.html
│ ├── place_order.html
│ ├── live_feed.html
├── flaskApp.py
├── dhan.py
├── live.py
├── requirements.txt
├── .env
└── README.md
```
