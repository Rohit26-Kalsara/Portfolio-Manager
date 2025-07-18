from abc import ABC, abstractmethod

# Abstract Asset class
class Asset(ABC):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @abstractmethod
    def calculate_return(self):
        pass

# Stock class
class Stock(Asset):
    def __init__(self, name, amount, current_price, purchase_price):
        super().__init__(name, amount)
        self.current_price = current_price
        self.purchase_price = purchase_price

    def calculate_return(self):
        return (self.current_price - self.purchase_price) * self.amount
    
# MutualFund class
class MutualFund(Asset):
    def __init__(self, name, amount, nav_purchase, nav_current):
        super().__init__(name, amount)
        self.nav_purchase = nav_purchase
        self.nav_current = nav_current

    def calculate_return(self):
        return (self.nav_current - self.nav_purchase) * self.amount

# Crypto class
class Crypto(Asset):
    def __init__(self, name, amount, purchase_price, current_price):
        super().__init__(name, amount)
        self.purchase_price = purchase_price
        self.current_price = current_price

    def calculate_return(self):
        return (self.current_price - self.purchase_price) * self.amount


# Bond class
class Bond(Asset):
    def __init__(self, name, amount, interest_rate, years):
        super().__init__(name, amount)
        self.interest_rate = interest_rate
        self.years = years

    def calculate_return(self):
        return self.amount * (self.interest_rate / 100) * self.years

# Portfolio class
class Portfolio:
    def __init__(self, owner):
        self.owner = owner
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def total_return(self):
        return sum([asset.calculate_return() for asset in self.assets])

    def show_portfolio(self):
        print(f"Portfolio for {self.owner}:\n")
        for asset in self.assets:
            print(f"{asset.name}: Return = ₹{asset.calculate_return():.2f}")

# ------------- SAMPLE USAGE ------------------

if __name__ == "__main__":
    # Create investor portfolio
    portfolio = Portfolio("Rohit")

    # Add Stock, Bond, MF, Crypto
    portfolio.add_asset(Stock("TCS", 10, 3700, 3300))
    portfolio.add_asset(Bond("SBI Bond", 50000, 6.5, 3))
    portfolio.add_asset(MutualFund("HDFC Mutual Fund", 100, 50, 65))
    portfolio.add_asset(Crypto("Bitcoin", 0.1, 3000000, 3200000))

    # Show portfolio and returns
    portfolio.show_portfolio()
    print(f"\nTotal Return: ₹{portfolio.total_return():.2f}")
   
