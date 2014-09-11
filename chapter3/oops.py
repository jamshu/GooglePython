class bank:
 account={}
 def account_init (name):
       account[name]=0
       print account[name]
 def deposit(name, amount):
       account[name] += amount
       print 'balance of ',name,account[name]

 def withdraw(name, amount):
       account[name] -= amount
       print 'balace of ',name,account[name]
a=bank()
account_init('ashif')
account_init('faizal')
deposit('ashif',100)
deposit('ashif',300)
withdraw('ashif',50)
withdraw('faizal',56)
