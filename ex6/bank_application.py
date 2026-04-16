class BankCustomer:
  def __init__(self,name,acc_no,initial_balance):
    self.name = name
    self.account = self.BankAccount(acc_no,initial_balance)
  def display(self):
    print("CUSTOMER NAME:",self.name)
    print("ACCOUNT NUMBER:",self.account.acc_no)
    print("BALANCE:",self.account.balance)
  class BankAccount:
    def __init__(self,acc_no,balance):
      self.acc_no = acc_no
      self.balance = balance
    def deposit(self,amount):
      if amount>0:
       self.balance += amount
       print("Rs",amount,"DEPOSITTED SUCESSFULLY!")
      else:
       print("INVALID AMOUNT Rs",amount,"TO DEPOSIT!")
    def withdraw(self,amount):
      if amount>0 and amount<=self.balance:
       self.balance -= amount
       print("Rs",amount,"WITHDRAWN SUCESSFULLY!")
      else:
       print("INSUFFICIENT AMOUNT Rs",amount,"TO WITHDRAW FROM Rs",self.balance)
    def get_balance(self):
      return self.balance
while True:
  name = input("ENTER THE NAME:")
  acc_no = input("ENTER THE ACCOUNT NUMBER:")
  initial_balance = float(input("ENTER THE INITIAL BALANCE:"))
  cus = BankCustomer(name,acc_no,initial_balance)
  cus.display()
  while True:
   print("MENU")
   print("1.TO DEPOSIT\n2.TO WITHDRAW\n3.TO CHECK BALANCE")
   ch = int(input("ENTER YOUR CHOICE(1-3):"))
   if ch==1:
    amount = float(input("ENTER THE AMOUNT TO DEPOSIT:"))
    cus.account.deposit(amount)
   elif ch==2:
    amount = float(input("ENTER AMOUNT TO WITHDRAW:"))
    cus.account.withdraw(amount)
   elif ch==3:
    print("CURRENT BALANCE IS Rs",cus.account.get_balance())
   else:
    print("INVALID CHOICE!")
    break
  choice = input("DO YOU WANT TO CONTINUE(Y/N):")
  if choice=="Y":
     continue
  else:
     print("THE END")
     break
