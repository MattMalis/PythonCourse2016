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

class Asset():
	def __init__(self, share_price, symbol):
		self.symbol = symbol
		self.share_price = share_price
		
class AssetAccount():
	def __init__(self, portfolio, asset_type=None):
		self.asset_list = {}
		self.portfolio = portfolio
		self.asset_type = asset_type
	
	def addAsset(self, shares, asset):
		if shares<0:
			return self.removeStock(-shares, asset)
		if asset in self.asset_list:
			self.asset_list[asset]+=shares
		else: self.asset_list[asset] = shares
	def removeAsset(self, shares, asset):
		if shares<0:
			return self.addStock(-shares, asset)
		if not asset in self.asset_list.keys():
			raise CustomException("cannot sell shares of %s, because you currently do not own any" %(asset.symbol))
		if self.asset_list[asset]<shares:
			raise CustomException("cannot sell more shares of a %s than currently in portfolio" %(self.asset_type))
		self.asset_list[asset] -= shares
	
	def __str__(self):
		asset_report = ""
		for a in self.asset_list:
			asset_report += '\t' + str(self.asset_list[a]) + " shares of " + str(a.symbol) + " priced at $" + str(a.share_price) + ' each \n'
		return "%s account for portfolio named %s contains: \n %s" %(self.asset_type, self.portfolio, asset_report)

class StockAccount(AssetAccount):
	def __init__(self, portfolio):
		AssetAccount.__init__(self, portfolio, "stock")
		
	
	def addStock(self, shares, stock):
		if not isinstance(stock, Stock):
			raise CustomException("attempt to add object to stock account that was not an instance of class Stock")
		if not isinstance(shares, int):
			raise CustomException("can only buy/sell stocks by whole shares (integer values)")
		return self.addAsset(shares, stock)
	
	def removeStock(self, shares, stock):
		if not isinstance(stock, Stock):
			raise CustomException("attempt to remove object from stock account that was not an instance of class Stock")
		if not isinstance(shares, int):
			raise CustomException("can only buy/sell stocks by whole shares (integer values)")
		return self.removeAsset(shares, stock)
		
class Stock(Asset):
	def __init__(self, share_price, symbol):
		Asset.__init__(self, share_price, symbol)
		
class MutualFundAccount(AssetAccount):
	def __init__(self, portfolio):
		AssetAccount.__init__(self, portfolio, "mutual fund")
		
	def addMF(self, shares, mf):
		if not isinstance(mf, MutualFund):
			raise CustomException("attempt to add object to mutual fund account that was not an instance of class MutualFund")
		return self.addAsset(shares, mf)

	def removeMF(self, shares, mf):
		if not isinstance(mf, MutualFund):
			raise CustomException("attempt to remove object from mutual fund account that was not an instance of class MutualFund")
		return self.removeAsset(shares, mf)
		
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
			for item in self.stock_account.asset_list.keys(): ## check to see if it is the stock symbol of one of the portfolio's stocks
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
			for item in self.mutual_fund_account.asset_list.keys():
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
	portfolio.mutual_fund_account.asset_list[MutualFund("DNE")] = 30
	#portfolio.sellMutualFund(45, "DNE")
	portfolio.sellMutualFund(25, "DNE")
	portfolio.buyStock(3, Stock(18.5, "MIM"))
	#print(portfolio)
	portfolio.withdrawCash(100)
	portfolio.sellStock(3, "MIM")
	ibm = Stock(76, "IBM")
	#portfolio.sellStock(8, "IBM")
	portfolio.sellStock(8, ibm)
	portfolio.history()
except CustomException as inst:
	print("\nError: %s" %(inst.value))
		
		
		
		
		
		
		
		
		