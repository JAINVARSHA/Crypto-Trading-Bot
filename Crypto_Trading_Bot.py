import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
import sys

# Setup logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            # Calculate notional value (price × quantity)
            if order_type == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT order.")
                notional = price * quantity
            elif order_type == "MARKET":
                # Fetch estimated market price
                ticker = self.client.futures_symbol_ticker(symbol=symbol)
                estimated_price = float(ticker['price'])
                notional = estimated_price * quantity
            else:
                raise ValueError("Invalid order type. Use 'MARKET' or 'LIMIT'.")

            # Check minimum notional
            if notional < 100:
                print(f"Order rejected: Notional value ${notional:.2f} is below the minimum of $100.")
                return None

            # Create the order
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce='GTC'
                )

            logging.info(f"Order placed successfully: {order}")
            print("Order placed successfully!")
            print(f"Order ID: {order['orderId']}")
            print(f"Status: {order['status']}")
            print(f"Executed Quantity: {order['executedQty']}")
            return order

        except BinanceAPIException as e:
            logging.error(f"Binance API Exception: {e.message}")
            print(f"Binance API Error: {e.message}")
        except Exception as e:
            logging.error(f"General Exception: {str(e)}")
            print(f"Error: {str(e)}")

            
#Command-line Interface
def get_user_input():
    print("\nWelcome to Binance Futures Testnet Trading Bot")
    print("⚠ Make sure your quantity × price ≥ $100, or your order will be rejected.\n")

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper().strip()
    
    while True:
        side = input("Order Side (BUY/SELL): ").upper().strip()
        if side in ["BUY", "SELL"]:
            break
        print("Invalid input. Please enter BUY or SELL.")

    while True:
        order_type = input("Order Type (MARKET/LIMIT): ").upper().strip()
        if order_type in ["MARKET", "LIMIT"]:
            break
        print("Invalid input. Please enter MARKET or LIMIT.")

    while True:
        try:
            quantity = float(input("Quantity: ").strip())
            if quantity > 0:
                break
            else:
                print("Quantity must be positive.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    price = None
    if order_type == "LIMIT":
        while True:
            try:
                price = float(input("Limit Price: ").strip())
                if price > 0:
                    break
                else:
                    print("Price must be positive.")
            except ValueError:
                print("Invalid price. Please enter a number.")

    return symbol, side, order_type, quantity, price


def main():
    # Use your testnet API credentials
    api_key = 'd8a1f0d16592d37dc7e3bf095e272e5863c58abba43e818e007e43560863a53f'
    api_secret = 'c10275c73152808c74eb2bfe6653b3262568e79e43857a22767f9c1b76868c29'

    bot = BasicBot(api_key, api_secret, testnet=True)

    symbol, side, order_type, quantity, price = get_user_input()
    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
