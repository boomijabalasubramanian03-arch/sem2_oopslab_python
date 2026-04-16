class Package:
  def __init__(self,pname,mode,cost):
    self.pname = pname
    self.mode = mode
    self.cost = cost
  def display_info(self):
    print("NAME :",self.pname)
    print("MODE OF TRANSPORT:",self.mode)
    print("COST IS :",self.cost)
class Adventure_Package(Package):
  def __init__(self,pname,mode,cost,adcost):
    super().__init__(pname,mode,cost)
    self.adcost = adcost
  def display_cost(self):
    super().display_info()
    print("TOTAL COST:",self.cost+self.adcost)
class Customer:
  def __init__(self,cname,package):
    self.cname = cname
    self.package = package
  def show(self):
    self.adcost = adcost
  def display_cost(self):
    super().display_info()
    print("TOTAL COST:",self.cost+self.adcost)
class Customer:
  def __init__(self,cname,package):
    self.cname = cname
    self.package = package
  def show(self):
    self.package.display_cost()
    print("CUSTOMER NAME:",self.cname)
pnamt
= input("ENTER PACKAGE NAME:")
mode = input("ENTER MODE OF TRANSPORT:")
cost = int(input("ENTER COST:"))
cname = input("ENTER CUSTOMER NAME:")
adcost = int(input("ENTER ADVENTURE COST:"))
package = Adventure_Package(pname,mode,cost,adcost)
c1 = Customer(cname,package)
c1.show()
