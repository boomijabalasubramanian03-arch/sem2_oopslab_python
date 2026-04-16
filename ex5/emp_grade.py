class emp:
   def __init__(self,empn,emps):
      self.empn = empn
      self.emps = emps
   def display(self):
      print("EMPLOYEE NAME:",self.empn)
      print("EMPLOYEE SALARY:",self.emps)
   def cal_grade(self):
     if self.emps >= 80000:
      print("GRADE PAY IS 8")
     elif self.emps >= 70000:
      print("GRADE PAY IS 7")
     elif self.emps >= 60000:
      print("GRADE PAY IS 6")
     else:
      print("CONSOLIDATED")
n = int(input("ENTER NO OF EMPLOYEES:"))
for i in range(n):
   empn = input("ENTER EMPLOYEE NAME:")
   emps = int(input("ENTER EMPLOYEE SALARY:"))
   e = emp(empn,emps)
   e.display()
   e.cal_grade()
