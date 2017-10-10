#simple banking Application
def validate_cash(price):
		if not isinstance(price,(int,float)): 
			raise TypeError("Cash must be numeric")
		elif price<0:
			raise TypeError("Cash should be positive")

class creditCard():
	def __init__(self,cutomer,bank,acnt,limit):
		self.cutomer = cutomer
		self.bank = bank
		self.acnt = acnt
		self.limit =limit
		self.balance=0
	def get_customer(self):
		return self.cutomer
	def get_bank(self):
		return self.bank
	def get_acnt(self):
		return self.acnt
	def get_limit(self): 
		return self.limit
	def get_balance(self):
		return self.balance
	def Deposite(self,price):
		validate_cash(price)
		if price + self.balance > self.limit:
			return False
		else:
			self.balance+=price
			return True
	def withdraw(self,price):
		validate_cash(price)
		if price >= self.balance:
			raise TypeError("price should be in limit")
		else:
			self.balance-=price
			return True

cc=creditCard('cm','BOM',121,10000)
print "cutomer details are as follows"
print "Name\t Bank\t Account\t Balance\n",cc.get_customer(),"\t ",cc.get_bank(),"\t ",cc.get_acnt(),"\t\t",cc.get_balance()
print "Balance Deposite: ",cc.Deposite(1000)
print "Your balance is: ",cc.get_balance()
print "Your withdraw is: ",cc.withdraw(100)
print "Your balance is: ",cc.get_balance()

#for Multiple Accounts
wallet=[]			
wallet.append(creditCard('vm','Dena',124,10000))
wallet.append(creditCard('srb','SBI',111,10000))
wallet.append(creditCard('sv','HDFC',111,10000))
print "Balance Deposite to : ",wallet[1].get_customer(),wallet[1].Deposite(1000)
print "\n\nName\t Bank\t Account\t Balance\n"
for x in range(len(wallet)):
	print wallet[x].get_customer(),"\t ", wallet[x].get_bank(),"\t ", wallet[x].get_acnt(),"\t\t", wallet[x].get_balance()

# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its num-
# ber of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower():
	def __init__(self,name,no_of_petals,price):
		self.name = name
		self.no_of_petals = no_of_petals
		self.price = price
	def get_name(self):	return self.name
	def get_petals(self): return self.no_of_petals
	def get_price(self): return self.price
	def change_price(self,name,price):
		if self.name==name:
			self.price=price
		else:
		 print "No flower of name",name
obj=Flower('Rose',10,100)
print "\n\nDetails of Flower:"
print "Name\t No_of_petals\t Price\n",obj.get_name(),"\t  ",obj.get_petals(),"\t\t",obj.get_price()
obj.change_price('Rose',55)
print "new price: ",obj.get_price()