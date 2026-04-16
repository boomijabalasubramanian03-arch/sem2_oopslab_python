class InsufficientFundsException(Exception):
   def __init__(self,msg = "Withdrawal failed : Insufficient funds!"):
      self.msg = msg
class MinimumBalanceException(Exception):
   def __init__(self,msg = "Withdrawal failed : Reached minimum balance!"):
      self.msg = msg
class Bank:
   def __init__(self,account_holder,balance):
      self.account_holder = account_holder
      self.balance = balance
   def deposit(self,amount):
     if amount<=0:
      print("DEPOSIT AMOUNT MUST BE POSITIVE:")
     else:
      self.balance += amount
      print("Rs",amount,"depsited successfully! New Balance:",self.balance)
   def withdrawal(self,amount):
     if amount>self.balance:
      raise InsufficientFundsException()
     elif self.balance-amount<500:
      raise MinimumBalanceException()
     else:
      self.balance -= amount
      print("Rs",amount,"withdrawed successfully! Remaining balance:",self.balance)
   def check_balance(self):
      print("Account balance : Rs",self.balance)
try:
   name = input("ENTER NAME:")
   ba = int(input("ENTER THE BALANCE AMOUNT:"))
   da = int(input("ENTER THE AMOUNT TO DEPOSIT:"))
   wa = int(input("ENTER THE AMOUNT TO WITHDRAW:"))
   account = Bank(name,ba)
   account.check_balance()
   account.deposit(da)
   account.withdrawal(wa)
except InsufficientFundsException as i:
   print("Exception :",i.msg)
except MinimumBalanceException as m:
   print("Exception :",m.msg)
except ValueError:
   print("Invalid input! please enter a valid number")
