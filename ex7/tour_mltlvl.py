class Place:
  def __init__(self,place):
    self.place = place
  def display_place(self):
    print("PLACE TO VISIT",self.place)
class Package_amount(Place):
  def __init__(self,place,n_days,n_people,chpd):
    super().__init__(place)
    self.n_days = n_days
    self.n_people = n_people
    self.chpd = chpd
  def calc_charge(self):
    return self.n_days*self.n_people*chpd
  def display_cost(self):
    self.display_place()
    print("TOTAL COST IS",self.calc_charge())
class Tour_guider(Package_amount):
  def __init__(self,place,n_days,n_people,chpd,guider,exp):
    super().__init__(place,n_days,n_people,chpd)
    self.guider = guider
    self.exp = exp
  def display_all(self):
    self.display_cost()
    print("TOUR GUIDER:",self.guider)
    print("GUIDERS EXPERIENCE:",self.exp)
print("\t\tAVAILABLE PLACES")
print("1.COORG\n2.HIMACHAL\n3.SHIMLA\n4.GOA\n5.LADAKH")
while True:
  place = input("ENTER THE PLACE YOU WANT TO VISIT:")
  n_days = int(input("ENTER NO OF DAYS:"))
  n_people = int(input("ENTER NO OF PEOPLE:"))
  guider = input("ENTER GUIDER NAME:")
  exp = int(input("ENTER GUIDER EXPERIENCE:"))
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   chpd=6000
  elif ch==2:
   chpd=8000
  elif ch==3:
   chpd=7000
  elif ch==4:
   chpd=5500
  elif ch==5:
   chpd=7500
  else:
   print("INVALID CHOICE")
  tour = Tour_guider(place,n_days,n_people,chpd,guider,exp)
  tour.display_all()
  choice = input("DO YOU WANT EXPLORE MORE(Y/N):")
  if choice == "Y":
   continue
  else:
   print("THANK YOU!")
   break
