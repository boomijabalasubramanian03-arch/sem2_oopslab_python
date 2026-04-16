class Tourism:
  def __init__(self,pname,duration,cost):
    self.pname = pname
    self.duration = duration
    self.cost = cost
  def display_pack(self):
    print("PACKAGE NAME:",self.pname)
    print("NO OF DAYS:",self.duration)
    print("COST OF PACKAGE:",self.cost)
class Family_Package(Tourism):
  def __init__(self,pname,duration,kidsdis,cost):
    super().__init__(pname,duration,cost)
    self.kd = kidsdis
  def total_cost(self):
    return self.cost*(self.kd/100)
  def display_family(self):
    self.display_pack()
    print("KIDS DISCOUNT:",self.kd,"%")
    print("TOTAL COST :",self.total_cost())
class Adventure_package(Tourism):
  def __init__(self,pname,duration,cost,activity_cost):
    super().__init__(pname,duration,cost)
    self.acost = activity_cost
  def t_cost(self):
    return self.cost+self.acost
  def display_info(self):
    self.display_pack()
    print("TOTAL COST:",self.t_cost())
pname = input("ENTER PACKAGE NAME:")
ch = int(input("CHOOSE : 1.FAMILY PACKAGE / 2.ADVENTURE PACKAGE:"))
if ch==1:
 f = Family_Package(pname,duration,kidsdis,cost)
 f.display_family()
elif ch==2:
 ad = Adventure_package(pname,duration,cost,activity_cost)
 ad.display_info()
else:
 print("INVALID CHOICE")
