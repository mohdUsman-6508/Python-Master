class BankAccount:
  
  def __init__(self,owner,balance=0):
    self.owner=owner
    self.balance=balance

  def deposit(self,amount):
    self.balance+=amount
    print(f"{amount} deposited. New balance:{self.balance}")

  def withdraw(self,amount):
    if amount>self.balance:
      print(f"Insufficient balance")
    else:
      self.balance-=amount
      print(f"{amount} withdrawn. New balance:{self.balance} ")      

  def balance(self):
    return self.balance


acc1=BankAccount("David",1000)

acc1.deposit(1000)
acc1.withdraw(200)
print(acc1.balance)
