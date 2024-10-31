from Tracker import get_stock_data

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