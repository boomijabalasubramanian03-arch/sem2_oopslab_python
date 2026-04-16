import pickle
class Employee:
  def __init__(self,eno,ename,esal,eaddr):
    self.eno = eno
    self.ename = ename
    self.esal = esal
    self.eaddr = eaddr
  def display(self):
     print("EMPLOYE NO:",self.eno)
     print("EMPLOYEE NAME:",self.ename)
     print("EMPLOYEE SALARY:",esal)
     print("EMPLOYEE ADDRESS:",eaddr)
with open("file.dat","wb") as f:
  while True:
    ename = input("ENTER EMPLOYEE NAME:")
    eno = int(input("ENTER EMPLOYEE NO:"))
    esal = int(input("ENTER EMPLOYEE SALARY:"))
    eaddr = input("ENTER EMPLOYEE ADDRESS:")
    e = Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
    print("PICKLING PERFORMED!")
    ch = input("DO YOU WANT TO COPNTINUE(Y/N):")
    if ch=="Y":
     continue
    else:
     print("END!")
     break
with open("file.dat","rb") as f:
  obj = pickle.load(f)
  print("UNPICKLING PERFORMED!")
  obj.display()
