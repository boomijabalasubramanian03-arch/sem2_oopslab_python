class Student:
   def __init__(self):
      self.tot = 0
      self.avg = 0
   def In(self):
      self.name = input("ENTER THE NAME:")
      self.rn = int(input("ENTER ROLL NO:"))
      self.mark1 = float(input("ENTER MARK1:"))
      self.mark2 = float(input("ENTER MARK2:"))
      self.mark3 = float(input("ENTER MARK3:"))
   def average(self):
      self.tot = self.mark1 + self.mark2 + self.mark3
      self.avg = self.tot/3
   def display(self):
      print(self.name,"\t",self.rn,"\t",self.mark1,"\t",self.mark2,"\t",self.mark3,end="    ")
      self.average()
      print(self.tot,"\t",self.avg)
n = int(input("ENTER THE NO OF STUDENTS:"))
for i in range(n):
   S = Student()
   S.In()
   print("NAME\tROLL NO\tMARK1\tMARK2\tMARK3\tTOTAL\tAVERAGE")
   S.display()
