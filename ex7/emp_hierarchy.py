class Employee:
  def __init__(self,name,eid):
    self.name = name
    self.eid = eid
  def display_name(self):
    print("NAME OF THE EMPLOYEE IS ",self.name)
    print("EMPLOYEE ID IS ",self.eid)
class Dailywage_employee(Employee):
  def __init__(self,name,eid,w_days,daily_wage):
    super().__init__(name,eid)
    self.daily_wage = daily_wage
    self.w_days = w_days
  def dailywage_calc(self):
    return self.daily_wage*w_days
class Monthlywage_employee(Employee):
  def __init__(self,name,eid,experience):
    super().__init__(name,eid)
    self.experience = experience
    self.mon_sal = 0
    self.hra = 0.5;self.da=0.2;self.a=1000;self.red=0.11
  def monthlysal_calc(self):
    if self.experience<=10:
     bp = 80000
     self.mon_sal += bp+(bp*self.hra)+(bp*self.da)+salf.a-(bp*self.red)
     return self.mon_sal
    elif self.experience>10 and self.experience>=15:
     bp = 100000
     self.mon_sal += bp+(bp*self.hra)+(bp*self.da)+self.a-(bp*self.red)
     return self.mon_sal
    elif self.experience>15 and self.experience>=20:
     bp = 120000
     self.mon_sal += bp+(bp*self.hra)+(bp*self.da)+salf.a-(bp*self.red)
     return self.mon_sal
    else:
     bp = 150000
     self.mon_sal += bp+(bp*self.hra)+(bp*self.da)+salf.a-(bp*self.red)
     return self.mon_sal
name = input("ENTER NAME OF THE EMPLOYEE:")
eid = input("ENTER EMPLOYEE ID:")
emp = input("ENTER DAILYWAGE OR MONTHLY PAID EMPLOYEE(D/M):")
if emp=="D":
 daily_wage = int(input("ENTER AMOUNT:"))
 w_days = int(input("ENTER THE NO OF DAYS:"))
 obj = Dailywage_employee(name,eid,w_days,daily_wage)
 obj.display_name()
 print("SALARY IS :",obj.dailywage_calc())
elif emp=="M":
 experience = int(input("ENTER EXPERIENCE:"))
 obj = Monthlywage_employee(name,eid,experience)
 obj.display_name()
 print("SALARY OF THE EMPLOYEE IS:",obj.monthlysal_calc())
else:
 print("INVALID CHOICE!")
