class studbill:
   def __init__(self):
      self.bill = 0
      self.ds = 20000
      self.dv = 28000
      self.hos = 62000
      self.tu = 55000
   def IN(self):
      self.name = input("ENTER NAME:")
      self.rollno = int(input("ENTER ROLL NUMBER:"))
      self.H_D = input("ENTER HOSTELLER OR DAYSCHOLAR:")
      if self.H_D=="D":
       self.bus = input("ENTER PLACE:")
   def cal_bill(self):
     if self.H_D == 'H':
      self.bill += self.tu+self.hos
     if self.H_D == 'D':
      if self.bus == 'V':
       self.bill += self.tu+self.dv
      if self.bus == 'S':
       self.bill += self.tu+self.ds
   def display(self):
      print("STUDENT NAME:",self.name)
      print("ROLL NUMBER:",self.rollno)
      print("HOSTELLAR / DAYSCHOLAR :",self.H_D)
      self.cal_bill()
      print("TOTAL BILL AMOUNT:",self.bill)
n = int(input("ENTER NO OF STUDENTS:"))
for i in range(n):
   s = studbill()
   s.IN()
   s.cal_bill()
   s.display()
