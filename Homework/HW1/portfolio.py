import random

class CustomException(Exception): 
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value

class CashAccount():		
	def __init__(self, portfolio, amount):
		self.portfolio = portfolio
		self.amount = amount
	def add(self, amount_added):
		if self.amount+amount_added<0:
			raise CustomException("transaction will result in negative cash balance")
		self.amount+=amount_added
	def subtract(self, amount_subtracted):
		return self.add(- int(amount_subtracted))
	
	def __str__(self):
		return "Cash account for portfolio named %s contains: \n\t$%s in cash\n" %(self.portfolio, self.amount)
		
class StockAccount():
	def __init__(self, portfolio):
		self.stock_list = {}
		self.portfolio = portfolio
	
	def addStock(self, shares, stock):
		if not isinstance(stock, Stock):
			raise CustomException("attempt to add object to stock account that was not an instance of class Stock")
		if not isinstance(shares, int):
			raise CustomException("can only buy/sell stocks by whole shares (integer values)")
		if shares<0:
			return self.removeStock(-shares, stock)
		if stock in self.stock_list:
			self.stock_list[stock]+=shares
		else: self.stock_list[stock] = shares
	def removeStock(self, shares, stock):
		if not isinstance(shares, int):
			raise CustomException("can only buy/sell stocks by whole shares (integer values)")
		if shares<0:
			return self.addStock(-shares, stock)
		if self.stock_list[stock]<shares:
			raise CustomException("cannot sell more shares of a stock than currently in portfolio")
		self.stock_list[stock] -= shares
	
	def __str__(self):
		stock_report = ""
		for s in self.stock_list:
			stock_report += '\t' + str(self.stock_list[s]) + " shares of " + str(s.symbol) + " priced at $" + str(s.share_price) + ' each \n'
		return "Stock account for portfolio named %s contains: \n %s" %(self.portfolio, stock_report)

class Stock():
	def __init__(self, share_price, symbol):
		self.symbol = symbol
		self.share_price = share_price
		
class MutualFundAccount():
	def __init__(self, portfolio):
		self.mf_list = {}	
		self.portfolio = portfolio
	def addMF(self, shares, mf):
		if shares<0:
			return self.removeMF(-shares, mf)
		if mf.symbol in self.mf_list:
			self.mf_list[mf]+=shares
		else: self.mf_list[mf] = shares
	def removeMF(self, shares, mf):
		if shares<0:
			return self.addMF(-shares, mf)
		if self.mf_list[mf]<shares:
			raise CustomException("cannot sell more shares of a mutual fund than currently in portfolio")
		self.mf_list[mf] -= shares
	
	def __str__(self):
		mf_report = ""
		for mf in self.mf_list:
			mf_report += '\t' + str(self.mf_list[mf]) + " shares of " + str(mf.symbol) + " priced at $" + str(mf.share_price) + " each \n"
		return "Mutual fund account for portfolio named %s contains:\n%s" %(self.portfolio, mf_report)

		
class MutualFund():
	def __init__(self, symbol, share_price=1):
		self.symbol = symbol
		self.share_price = share_price
		
class Portfolio():
	def __init__(self, client=" "):
		self.client = client
		self.cash_account = CashAccount(client, 0)
		self.stock_account = StockAccount(client)
		self.mutual_fund_account = MutualFundAccount(client)
		self.transactions = []
	
	def addCash(self, amount_added):
		self.cash_account.add(amount_added)
		self.transactions.append("Added $%s to cash account" %(amount_added))
	def withdrawCash(self, amount_subtracted):
		self.cash_account.subtract(amount_subtracted)
		self.transactions.append("Withdrew $%s from cash account" %(amount_subtracted))
	
	def buyStock(self, shares, stock):
		self.withdrawCash(shares * stock.share_price)
		self.stock_account.addStock(shares, stock)
		self.transactions.append("Bought %s shares of stock %s at share price of %s" %(shares, stock.symbol, stock.share_price))
		
	def sellStock(self, shares, stock):
		if not isinstance(stock, Stock): ## if arg is not of class Stock
			for item in self.stock_account.stock_list.keys(): ## check to see if it is the stock symbol of one of the portfolio's stocks
				if item.symbol == stock:
					stock = item ## ...and swap the symbol fo for the stock object itself
					break
			else: raise CustomException("Error: attempt to remove stock that is not currently in stock_list")
		self.stock_account.removeStock(shares, stock)
		sellPrice = round((random.uniform(.5, 1.5))*stock.share_price,2)
		self.transactions.append("Sold %s shares of stock %s at share price of %s" %(shares, stock.symbol, sellPrice))
		self.addCash(shares * sellPrice)
	
	def buyMutualFund(self, shares, mf):
		self.withdrawCash(shares*mf.share_price)
		self.mutual_fund_account.addMF(shares, mf)
		self.transactions.append("Bought %s shares of mutual fund %s at share price of %s" %(shares, mf.symbol, mf.share_price))
		
	def sellMutualFund(self, shares, mf):
		if not isinstance(mf, MutualFund):
			for item in self.mutual_fund_account.mf_list.keys():
				if item.symbol == mf:
					mf = item
					break
			else: raise CustomException("attempt to remove mutual fund that is not currently in mutual_fund_list")
		self.mutual_fund_account.removeMF(shares, mf)
		sellPrice = round((random.uniform(.9,1.2))*mf.share_price,2)
		self.transactions.append("Sold %s shares of mutual fund %s at share price of %s" %(shares, mf.symbol, sellPrice))
		self.addCash(shares*mf.share_price)
	
	def history(self):
		for transaction in self.transactions:
			print transaction
		
	def __str__(self):
		return str(self.cash_account) + str(self.stock_account) + str(self.mutual_fund_account)
		
try:
	portfolio = Portfolio("Malis")
	portfolio.addCash(300.50)
	s = Stock(20, "HFH")
	portfolio.buyStock(5, s)
	mf1 = MutualFund("BRT")
	mf2 = MutualFund("GHT")
	portfolio.buyMutualFund(10.3, mf1)
	portfolio.buyMutualFund(2, mf2)
	print(portfolio)
	portfolio.sellMutualFund(3,"BRT")
	portfolio.sellStock(1,"HFH")
	portfolio.withdrawCash(50)
	portfolio.history()
	portfolio.mutual_fund_account.mf_list[MutualFund("DNE")] = 30
	#portfolio.sellMutualFund(45, "DNE")
	portfolio.sellMutualFund(25, "DNE")
	portfolio.buyStock(3, Stock(18.5, "MIM"))
	print(portfolio)
	portfolio.withdrawCash(100)
	portfolio.sellStock(3, "MIM")
	portfolio.history()
except CustomException as inst:
	print("\nError: %s" %(inst.value))
		
		
		
		
		
		
		
		
		