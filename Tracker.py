import requests
import numpy as np

API_KEY = '70LD2Y9SU10PI1M0'

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        return None

def calculate_gain_loss(initial_value, current_value):
    return current_value - initial_value


class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] -= quantity
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock_data = get_stock_data(symbol)
            if stock_data:
                price = float(stock_data['05. price'])
                total_value += price * quantity
        return total_value

def main():
    portfolio = Portfolio()
    initial_value = None
    
    while True:
        print("\n1. Add stock to portfolio")
        print("2. Remove stock from portfolio")
        print("3. View portfolio value")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            value = portfolio.get_portfolio_value()
            
            # Set initial value if not already set
            if initial_value is None:
                initial_value = value
            
            gain_loss = calculate_gain_loss(initial_value, value)
            print(f"Portfolio value: ${value:.2f}")
            print("Gains/Losses: ${:.2f}".format(gain_loss))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
