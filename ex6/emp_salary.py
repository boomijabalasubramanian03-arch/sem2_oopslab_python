class Employee:
  def __init__(self,name,bp,bonus,ded):
    self.name = name
    self.salary = self.Salaryemp(bp,bonus,ded)
  def display(self):
    print("EMPLOYEE NAME:",self.name)
    print("GROSS SALARY:",self.salary.gross_salary())
    print("NET SALARY:",self.salary.net_salary())
  class Salaryemp:
    def __init__(self,bp,bonus,ded):
      self.bp = bp
      self.bonus = bonus
      self.ded = ded
    def gross_salary(self):
      return self.bp + self.bonus
    def net_salary(self):
      return self.gross_salary()-(self.bp*(self.ded/100))
while True:
   name = input("ENTER THE NAME:")
   bp = float (input("ENTER THE BASIC PAY:"))
   bonus = float(input("ENTER THE BONUS AMOUNT:"))
   ded = float(input("ENTER THE DEDUCTION IN %:"))
   emp = Employee(name,bp,bonus,ded)
   emp.display()
   emp.salary.gross_salary()
   emp.salary.net_salary()
   ch = input("DO YOU WANT TO CONTINUE(Y/N):")
   if ch=="Y":
      continue
   else:
      print("THANK YOU!")
      break
