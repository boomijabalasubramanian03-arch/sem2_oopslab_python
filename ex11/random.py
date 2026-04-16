from random import *
class randomerror(Exception):
   def __init__(self,msg = "ERROR:NUMBER LESS THAN 0.1!"):
      self.msg = msg
class randgen:
   def __init__(self,n):
      self.n = n
   def display(self):
     for i in range(self.n):
      self.number = random()
     if self.number < 0.1:
      raise randomerror
     else:
      print(self.number)
n = int(input("ENTER NUMBER OF GENERATION NEEDED:"))
obj = randgen(n)
for i in range(n):
   obj.display()
