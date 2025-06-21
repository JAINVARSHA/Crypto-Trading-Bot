
# Binance Futures Testnet Trading Bot

This project is a simplified automated trading bot built in Python that interacts with the **Binance Futures Testnet API** using the `python-binance` library.

It allows users to place `MARKET` or `LIMIT` orders based on their input, with proper logging, error handling, and minimum notional checks.

---

## Features

- Connects to Binance **Futures Testnet**.
- Places **MARKET** or **LIMIT** orders via terminal.
- Enforces **minimum notional value** of $100 (price × quantity).
- Logs all API activity and errors to `bot.log`.
- Modular and beginner-friendly Python code.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/basic-bot.git
cd basic-bot
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

**requirements.txt** content:

```
python-binance==1.0.17
```

---

## Get Your Binance Testnet API Keys

1. Go to [https://testnet.binancefuture.com/](https://testnet.binancefuture.com/)
2. Register/Login and get your API Key and Secret from the account settings.
3. Replace your API key and secret in the `main()` function of `basic_bot.py`.

---

## Usage

Run the script using:

```bash
python basic_bot.py
```

You will be prompted for:

- Symbol (e.g., BTCUSDT)
- Order side (BUY/SELL)
- Order type (MARKET/LIMIT)
- Quantity
- Price (for LIMIT orders)

---

## File Structure

```
basic-bot/
├── basic_bot.py         # Main trading bot script
├── bot.log              # Log file (auto-generated)
├── requirements.txt     # Python dependencies
└── README.md            # Documentation file (this file)
```

---

## Sample Log (`bot.log`)

```
2025-06-21 16:10:25,321:INFO:Order placed successfully: {'orderId': 12345678, ...}
2025-06-21 16:11:01,900:ERROR:Binance API Exception: Order quantity too low.
```

---

## Disclaimer

This bot is for **educational purposes only**. It interacts with the Binance **Futures Testnet** and **will not execute real trades**. Always test thoroughly and use responsibly.

---

## Contact

**Author**: Varsha Jain  
Email: varsha.jain@email.com  
GitHub: [https://github.com/JAINVARSHA](https://github.com/JAINVARSHA)

---

Happy Trading!
