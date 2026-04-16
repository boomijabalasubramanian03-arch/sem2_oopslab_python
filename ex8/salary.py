class  Employee:
    def __init__(self,name="",sal=0):
        self.name = name
        self.sal = sal
    def __add__(self,var):
        e3 = Employee()
        e3.name = self.name +"&"+var.name
        e3.sal = self.sal + var.sal
        return e3
    def __sub__(self,var):
        e3 = Employee()
        e3.name = self.name +"&"+var.name
        e3.sal = self.sal - var.sal
        return e3
    def __mul__(self,var):
        e3 = Employee()
        e3.name = self.name +"&"+var.name
        e3.sal = (self.sal + var.sal)*12
        return e3
    def __gt__(self,var):
        e3 = Employee()
        e3.name = self.name +"&"+var.name
        e3.sal = self.sal > var.sal
        return e3
    def display(self):
        print("NAME OF THE EMPLOYEE:",self.name)
        print("SALARY OF THE EMPLOYEE:",self.sal)
print("1.SALARY ADDITION\n2.SALARY SUBTRACTION\n3.ANNUAL SALARY\n4.HIGHEST SALARY")
while True:
    n1= input("ENTER FIRST EMPLOYEE NAME:")
    n2 = input("ENTER SECOND EMPLOYEE NAME:")
    sal1 = float(input("ENTER FIRST EMPLOYEE SALARY:"))
    sal2 = float(input("ENTER SECOND EMPLOYEE SALARY:"))
    n = int(input("ENTER YOUR CHOICE:"))
    if n==1:
        e1 = Employee(n1,sal1)
        e2 = Employee(n2,sal2)
        res = e1+e2
    elif n==2:
        e1 = Employee(n1,sal1)
        e2 = Employee(n2,sal2)
        res = e1-e2
    elif n==3:
        e1 = Employee(n1,sal1)
        e2 = Employee(n2,sal2)
        res = e1*e2
    elif n==4:
        e1 = Employee(n1,sal1)
        e2 = Employee(n2,sal2)
        res = e1>e2
    else:
        print("INVALID CHOICE!")
    print("DETAILS OF FIRST EMPLOYEE:")
    e1.display()
    print("DETAILS OF SECOND EMPLOYEE:")
    e2.display()
    print("RESULTANT VALUES")
    res.display()
    choice = input("DO YOU WANT TO CONTINUE(Y/N):")
    if choice=="Y":
        continue
    else:
        print("THANK YOU!")
        break
