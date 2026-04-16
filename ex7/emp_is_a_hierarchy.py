class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def display_info(self):
    print("NAME OF THE PERSON:",self.name)
    print("AGE OF THE PERSON:",self.age)
class Employee(Person):
  def __init__(self,name,age,empid,pos):
    super().__init__(name,age)
    self.empid = empid
    self.pos = pos
  def  display_employee(self):
    self.display_info()
    print("EMPLOYEE ID:",self.empid)
    print("POSITION OF THE EMPLOYEE:",self.pos)
class Company:
  def __init__(self,comp_name,emp):
    self.comp_name = comp_name
    self.emp = emp
  def show_comp(self):
    print("COMPNY NAME:",self.comp_name)
    print("EMPLOYEE INFO")
    self.emp.display_employee()
while True:
  name = input("ENTER PERSON NAME:")
  age = int(input("ENTER PERSON AGE:"))
  empid = int(input("ENTER EMPLOYEE ID:"))
  pos = input("ENTER POSITION:")
  comp_name = input("ENTER COMPANY NAME:")
  emp = Employee(name,age,empid,pos)
  comp = Company(comp_name,emp)
  comp.show_comp()
  ch = input("DO YOU WANT TO CONTINUE(Y/N):")
  if ch == "Y":
   continue
  else:
   print("THE END!")
   break
