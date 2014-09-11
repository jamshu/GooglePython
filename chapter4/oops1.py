class bankaccount:
 def __init__(name):
   name.balance=0
 def deposit(name,amount):
   name.balance=name.balance+amount
   print name.balance
 def withdraw(name,amount):
   name.balance=name.balance-amount
   print name.balance

ashif=bankaccount()
ashif.deposit(1000)
ashif.withdraw(300)
