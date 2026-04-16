class Person:
  def __init__(self,name):
    self.name = name
  def display_name(self):
    print("NAME OF THE STUDENT IS:",self.name)
class student(Person):
  def __init__(self,name,stid,m1,m2,m3):
    super().__init__(name)
    self.sid = sid
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3
  def totalmark(self):
    return self.m1+self.m2+self.m3
  def avgmark(self):
    return self.totalmark()/3
  def displayres(self):
    self.display_name()
    print("TOTAL MARKS IS :",self.totalmark())
    print("AVERAGE MARKS IS :",self.avgmark())
class graduate_student(student):
  def __init__(self,name,sid,m1,m2,m3,degree):
    super().__init__(name,sid,m1,m2,m3)
    self.degree = degree
  def check_eligibility(self):
    if self.avgmark()>=60:
     print("ELIGIBLE FOR THE DEGREE AWARD:",self.degree)
    else:
     print("NOT ELIGIBLE FOR THE DEGREE AWARD:",self.degree)
  def display_all(self):
    self.displayres()
    print("DEGREE:",self.degree)
    self.check_eligibility()
while True:
  name = input("ENTER THE STUDENT NAME:")
  sid = int(input("ENTER THE STUDENT ID:"))
  m1 = int(input("ENTER THE MARK 1:"))
  m2 = int(input("ENTER THE MARK 2:"))
  m3 = int(input("ENTER THE MARK 3:"))
  degree = input("ENTER THE DEGREE:")
  obj = graduate_student(name,sid,m1,m2,m3,degree)
  obj.display_all()
  ch = input("DO YOU WANT TO CONTINUE(Y/N):")
  if ch=="N":
   break
