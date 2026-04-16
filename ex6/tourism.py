class Tourism:
  def __init__(self,place,n_days,n_people,chd):
    self.place = place
    self.price = self.CalPrice(n_days,n_people,chd)
  def display(self):
    print("PLACE:",self.place)
    print("TOTAL COST:",self.price.calculate())
  class CalPrice:
    def __init__(self,n_days,n_people,chd):
      self.n_days = n_days
      self.n_people = n_people
      self.chd = chd
    def calculate(self):
      return self.n_days*self.n_people*self.chd
while True:
  print("\t\tAVALIABLE PLACES\t\t")
  print("1.GOA\n2.COORG\n3.HIMACHAL\n4.ARUNACHAL PRADESH")
  place = input("ENTER PLACE:")
  n_days = int(input("ENTER NO OF DAYS:"))
  n_people = int(input("ENTER NO OF PEOPLE:"))
  chd = float(input("ENTER THE CHARGE PER DAY:"))
  tour = Tourism(place,n_days,n_people,chd)
  tour.display()
  tour.price.calculate()
  ch = input("DO YOU WANT TO CONTINUE(Y/N):")
  if ch=="Y":
   continue
  else:
   print("THANK YOU!")
   break
