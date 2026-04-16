class emp:
   def __init__(self):
      self.sal=0
   def IN(self):
      self.en = input("ENTER EMPLOYEE NAME:")
      self.ei = int(input("ENTER EMPLOYEE ID:"))
      self.bp = int(input("ENTER BASIC PAY:"))
   def cal_sal(self):
      self.sal += (self.bp + (self.bp*0.2)+(self.bp*0.5)+1000)-(self.bp*0.11)
   def display(self):
      print("EMPLOYEE NAME:",self.en)
      print("EMPLOYEE ID:",self.ei)
      self.cal_sal()
      print("SALARY:",self.sal)
n = int(input("ENTER NO OF EMPLOYEES:"))
for i in range(n):
   e = emp()
   e.IN()
   e.display()
