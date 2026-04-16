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
print("\t\tAVAILABLE PLACES")
print("1.COORG\n2.HIMACHAL\n3.SHIMLA\n4.GOA\n5.LADAKH")
while True:
  place = input("ENTER THE PLACE YOU WANT TO VISIT:")
  n_days = int(input("ENTER NO OF DAYS:"))
  n_people = int(input("ENTER NO OF PEOPLE:"))
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   chpd=1500
  elif ch==2:
   chpd=4000
  elif ch==3:
   chpd=5000
  elif ch==4:
   chpd=2000
  elif ch==5:
   chpd=5500
  else:
   print("INVALID CHOICE")
  tour = Package_amount(place,n_days,n_people,chpd)
  tour.display_cost()
  choice = input("DO YOU WANT EXPLORE MORE(Y/N):")
  if choice == "Y":
   continue
  else:
   print("THANK YOU!")
   break
