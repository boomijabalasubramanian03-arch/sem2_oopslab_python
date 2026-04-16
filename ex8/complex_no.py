class  Complex:
    def __init__(self,real=0,img=0):
        self.real = real
        self.img = img
    def __add__(self,c2):
        c3 = Complex()
        c3.real = self.real + c2.real
        c3.img = self.img + c2.img
        return c3
    def __sub__(self,c2):
        c3 = Complex()
        c3.real = self.real - c2.real
        c3.img = self.img - c2.img
        return c3
    def __mul__(self,c2):
        c3 = Complex()
        c3.real = self.real * c2.real
        c3.img = self.img * c2.img
        return c3
    def display(self):
        print(self.real,"+",self.img,"i")
print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION")
while True:
    n1real = int(input("ENTER FIRST NUMBER REAL PART:"))
    n1img = int(input("ENTER FIRST NUMBER IMAGINARY PART:"))
    n2real = int(input("ENTER SECOND NUMBER REAL PART:"))
    n2img = int(input("ENTER SECOND NUMBER IMAGINARY PART:"))
    n = int(input("ENTER YOUR CHOICE:"))
    if n==1:
        c1 = Complex(n1real,n1img)
        c2 = Complex(n2real,n2img)
        res = c1+c2
    elif n==2:
        c1 = Complex(n1real,n1img)
        c2 = Complex(n2real,n2img)
        res = c1-c2
    elif n==3:
        c1 = Complex(n1real,n1img)
        c2 = Complex(n2real,n2img)
        res = c1*c2
    else:
        print("INVALID CHOICE!")
    print("FIRST COMPLEX NUMBER:")
    c1.display()
    print("SECOND COMPLEX NUMBER:")
    c2.display()
    print("RESULT")
    res.display()
    choice = input("DO YOU WANT TO CONTINUE(Y/N):")
    if choice=="Y":
        continue
    else:
        print("THANK YOU!")
        break
