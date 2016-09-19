# oops debit card program
import sqlite3
class BankAccount:
	bankName="SBI"
	#balance=0
	def __init__(self, name,accountnumber):
		self.name=name
		self.accountnumber=accountnumber
		self.balance = 0
	def balance_show(self):
		print "balance in the account is %s"%(self.balance)
		print "name: ",self.name		
	def draw(self,amount):	
		self.balance=self.balance-amount
		print "Amount %s is drawn with balance %s"%(amount,self.balance)
		self.updateaccount()
	def deposit(self,amount):
		self.balance=self.balance+amount
		print "deposited amount is %s"%self.balance	
		self.updateaccount()
	def saveaccount(self):
		insertquery = "insert into BankAccount values('%s','%s','%s')"%(self.accountnumber,self.name,self.balance)
		Accountconnection=sqlite3.connect(r"D:\python\Commondb.db")
		Accountconnection.execute(insertquery)
		Accountconnection.commit()
		Accountconnection.close()
	def updateaccount(self):
		depositquery="update BankAccount set balance=%s where accountnumber=%s"%(self.balance,self.accountnumber) 
		Depositconnection=sqlite3.connect(r"D:\python\Commondb.db")
		Depositconnection.execute(depositquery)
		Depositconnection.commit()
		Depositconnection.close()
"""account1=BankAccount("Sunny",12345)
#account1.balance=0
account1.saveaccount()
account2.saveaccount()
account1.updateaccount()
account2.updateaccount()
account1.deposit(2000)
account1.balance_show()
account2=BankAccount("Swetha",74838)
#account2.balance=0
account2.deposit(3000)
account2.balance_show()		
account2.draw(500)
account2.balance_show()
account1.draw(1000)
account1.balance_show()"""


class CreditCardAccount(BankAccount):
	def __init__(self,name,accountnumber):
		self.accountnumber=accountnumber
		self.name=name
		self.balance=0				
"""useraccount1=CreditCardAccount("parul",18543)
useraccount1.updateaccount()
useraccount1.saveaccount()
useraccount1.draw(500)
useraccount1.balance_show()
useraccount1.saveaccount()

useraccount2=CreditCardAccount("vicky",94324)
useraccount2.updateaccount()
useraccount2.saveaccount()
useraccount2.draw(1000)
useraccount2.balance_show()
useraccount2.saveaccount()"""

useraccount3=CreditCardAccount("laalu",254323)
useraccount3.saveaccount()
useraccount3.draw(1000)
useraccount3.balance_show()


class DebitCardAccount(BankAccount):
	def __init__(self,name,accountnumber):
		self.accountnumber=accountnumber
		self.name=name
		self.balance=0				
firstuseraccount=DebitCardAccount("manu",228986)
firstuseraccount.saveaccount()
firstuseraccount.deposit(50000)
firstuseraccount.draw(500)
firstuseraccount.balance_show()
seconduseraccount=DebitCardAccount("chandu",8653)
seconduseraccount.saveaccount()
seconduseraccount.deposit(40000)
seconduseraccount.draw(1000)
seconduseraccount.balance_show()




				
