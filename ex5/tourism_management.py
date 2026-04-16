class tourism:
   tot_bookings = 0
   def __init__(self,place,n_days,n_people,price):
      self.place = place
      self.n_days = n_days
      self.n_people = n_people
      self.price = price
   @classmethod
   def  inc_bookings(cls):
      cls.tot_bookings += 1
   def calc_cost(self):
     self.tot_cost = self.n_people * self.n_days * self.price
     return self.tot_cost
   def details(self):
      print("PLACE :",self.place)
      print("DURATION :",self.n_days)
      print("PRICE PER PERSON:",self.price)
      print("TOTAL COST:",self.tot_cost)
   @classmethod
   def display(cls):
      print("TOTAL NO OF BOOKINGS MADE:",cls.tot_bookings)
   @staticmethod
   def available_places():
      print("\t\tAVAILABLE PLACES")
      print("1.Parris\n2.Rome\n3.Bali\n4.Tokyo\n5.New York")
tourism.available_places()
place = int(input("ENTER PLACE:"))
n_days = int(input("ENTER NO OF DAYS:"))
n_people = int(input("ENTER NO OF PEOPLE:"))
if place==1:
   price = 100000
if place==2:
   price = 90000
if place==3:
   price = 60000
if place==4:
   price = 45000
if place==5:
   price = 120000
tour = tourism(place,n_days,n_people,price)
tourism.inc_bookings()
tour.calc_cost()
tour.details()
tourism.display()
