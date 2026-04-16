class account:
 def __init__(self,acc_no,acc_holder,balance):
   self.acc_no = acc_no
   self.acc_holder = acc_holder
   self.balance = balance
 def display_info(self):
   print("ACCOUNT NUMBER IS ",self.acc_no)
   print("ACCOUNT HOLDER IS ",self.acc_holder)
   print("BALANCE AMOUNT IS ",self.balance)
 def deposit(self,amount):
   if amount>0:
    self.balance += amount
    print("AMOUNT Rs",amount,"DEPSITED SUCCESSFULLY")
   else:
    print("AMOUNT CANT BE NEGATIVE,ENTER PROPER AMOUNT!")
 def withdraw(self,amount):
   if amount>0 and self.balance>500:
    self.balance -= amount
    print("AMOUNT Rs",amount,"WITHDRAWN SUCCESSFULLY")
   else:
    print("INSUFFICIENT AMOUNT TO WITHDRAW!")
 def get_balance(self):
   return self.balance
class savingsacc(account):
 def __init__(self,acc_no,acc_holder,balance,interest_rate):
   super().__init__(acc_no,acc_holder,balance)
   self.interest_rate = interest_rate
 def add_interest(self):
   interest = self.balance * (self.interest_rate/100)
   self.balance += interest
   print("INTEREST",interest,"ADDED! NEW BALANCE IS",self.balance)
acc_no = input("ENTER THE ACCOUNT NUMBER:")
acc_holder = input("ENTER THE ACCOUNT HOLDER:")
balance = float(input("ENTER THE BALANCE AMOUNT:"))
interest_rate = float(input("ENTER THE INTEREST RATE IN %:"))
obj = savingsacc(acc_no,acc_holder,balance,interest_rate)
print("1.TO DEPOSIT\n2.TO WITHDRAW\n3.TO CHECK BALANCE\n4.TO ADD INTEREST")
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
    amount = float(input("ENTER AMOUNT TO DEPOSIT:"))
    obj.deposit(amount)
   elif ch==2:
    amount = float(input("ENTER AMOUNT TO WITHDRAW:"))
    obj.withdraw(amount)
   elif ch==3:
    print(obj.get_balance())
   elif ch==4:
    obj.add_interest()
   else:
    print("INVALID CHOICE")
    break
