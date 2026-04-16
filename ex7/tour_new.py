class Transport:
  def __init__(self,ttype,tcost):
    self.ttype = ttype
    self.tcost = tcost
  def display_transport(self):
    print("TRANSPORT TYPE :",self.ttype)
    print("COST IS :",self.tcost)
class Accomodation:
  def __init__(self,hotel_name,stay_cost):
    self.hname = hotel_name
    self.scost = stay_cost
  def display_hotel(self):
     print("HOTEL NAME :",self.hname)
     print("STAY COST :",self.scost)
class Tourism(Transport,Accomodation):
   def __init__(self,pname,ttype,tcost,hname,scost,duration):
     Transport.__init__(self,ttype,tcost)
     Accomodation.__init__(self,hname,scost)
     self.pname = pname
     self.duration = duration
   def total_cost(self):
     return self.scost+self.tcost
   def display_info(self):
     print("NAME OF THE PACKAGE:",self.pname)
     print("DURATION :",self.duration)
     self.display_transport()
     self.display_hotel()
     print("TOTAL COST :",self.total_cost())
print("WELCOME YOU ALL!")
while True:
   pname = input("ENTER THE PACKAGE NAME:")
   ttype = input("ENTER MODE OF TRANSPORT:")
   tcost = int(input("ENTER TRANSPORT COST FOR PACKAGE:"))
   hname = input("ENTER HOTEL NAME:")
   scost = int(input("ENTER THE STAY COST:"))
   duration = int(input("ENTER THE DURATION:"))
   p = Tourism(pname,ttype,tcost,hname,scost,duration)
   p.display_info()
   ch = input("DO YOU WANT TO CONTINUE(Y/N):")
   if ch=="Y":
    continue
   else:
    print("THE END!")
    break
