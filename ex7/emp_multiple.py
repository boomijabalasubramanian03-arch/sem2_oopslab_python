class Employee:
  def __init__(self,empid,pos):
    self.empid = empid
    self.pos = pos
  def display_emp(self):
    print("EMPLOYEE ID:",self.empid)
    print("POSITION:",self.pos)
class Student:
  def __init__(self,stdid,grade):
    self.stdid = stdid
    self.grade = grade
  def display_stud(self):
    print("STUDENT ID :",self.stdid)
    print("GRADE OF THE STUDENT:",self.grade)
class Research_scholar(Employee,Student):
  def __init__(self,name,empid,pos,stdid,grade,res_topic,supervisor):
    Employee.__init__(self,empid,pos)
    Student.__init__(self,stdid,grade)
    self.name = name
    self.res_topic = res_topic
    self.supervisor = supervisor
  def display_all(self):
    print("NAME OF THE PERSON:",self.name)
    self.display_emp()
    self.display_stud()
    print("RESEARCH TOPIC:",self.res_topic)
    print("SUPERVISOR NAME:",self.supervisor)
while True:
  name = input("ENTER NAME OF THE PERSON:")
  empid = input("ENTER EMPLOYEE ID:")
  pos = input("ENTER POSITION:")
  stdid = int(input("ENTER STUDENT ID:"))
  grade = input("ENTER GRADE:")
  res_topic = input("ENTER RESEARCH TOPIC:")
  supervisor = input("ENTER SUPERVISOR:")
  res_sch = Research_scholar(name,empid,pos,stdid,grade,res_topic,supervisor)
  res_sch.display_all()
  ch = input("DO YOU WANT TO CONTINUE(Y/N):")
  if ch=="Y":
   continue
  else:
   print("THE END!")
   break
