class Employee:
  def __init__(self,name):
    self.name = name
  def cal_sal(self):
    return "SALARY NOT DEFINED FOR BASE EMPLOYEE!"
  def display(self):
    print("EMPLOYEE TYPE:",self.__class__.__name__)
    print("EMPLOYEE NAME:",self.name)
    print("SALARY :",self.cal_sal())
class Parttime_employee:
  def __init__(self,name,hours,rate):
    Employee.__init__(self,name)
    self.hours = hours
    self.rate = rate
  def cal_sal(self):
    return self.hours*self.rate
  def display(self):
    print("EMPLOYEE TYPE:",self.__class__.__name__)
    print("EMPLOYEE NAME:",self.name)
    print("SALARY :",self.cal_sal())
class Fulltime_employee:
  def __init__(self,name,mon_sal):
    Employee.__init__(self,name)
    self.mon_sal = mon_sal
  def cal_sal(self):
    return self.mon_sal*12
  def display(self):
    print("EMPLOYEE TYPE:",self.__class__.__name__)
    print("EMPLOYEE NAME:",self.name)
    print("ANNUAL SALARY :",self.cal_sal())
print("=====CHOOSE=====")
print("1.PART TIME EMPLOYEE\n2.FULL TIME EMPLOYEE")
while True:
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   name = input("ENTER EMPLOYEE NAME:")
   hours = float(input("ENTER TOTAL HOURS:"))
   rate = float(input("ENTER RATE:"))
   e = Parttime_employee(name,hours,rate)
   e.display()
  elif ch==2:
   name = input("ENTER EMPLOYEE NAME:")
   mon_sal = float(input("ENTER MONTHLY SALARY:"))
   e = Fulltime_employee(name,mon_sal)
   e.display()
  else:
   name = input("ENTER EMPLOYEE NAME:")
   e = Employee(name)
   e.display()
  choice = input("DO YOU WANT TO CONTINUE(Y/N):")
  if choice=="Y":
   continue
  else:
   break
