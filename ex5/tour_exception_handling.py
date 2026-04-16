class InvalidInputError(Exception):
   def __init__(self,msg = "Value can't be negative or zero"):
      self.msg = msg
class Tourism:
   def __init__(self,place,numpeople,numdays,chargeperday):
      self.place = place
      self.numpeople = numpeople
      self.numdays = numdays
      self.chargeperday = chargeperday
      self.total = 0
   def validity(self,value):
     if value<=0:
      raise InvalidInputError
   def cal_cost(self,numpeople,numdays,chargeperday):
     self.validity(numpeople)
     self.validity(numdays)
     self.validity(chargeperday)
     self.total += numpeople*numdays*chargeperday
   @staticmethod
   def available_places():
     print("\t\tAVAILABLE PLACES")
     print("1.GOA\n2.SHIMLA\n3.GUJARAT")
   def display(self):
     print("PLACE:",self.place)
     print("CHARGE PER DAY:",self.chargeperday)
     print("NUMBER OF PEOPLE:",self.numpeople)
     print("NUMBER OF DAYS:",self.numdays)
     print("TOTAL AMOUNT:",self.total)
try:
   Tourism.available_places()
   place = input("ENTER PLACE:")
   numpeople = int(input("ENTER NO OF PEOPLE:"))
   numdays = int(input("ENTER NO OF DAYS:"))
   chargeperday = float(input("ENTER CHARGEPERDAY:"))
   tour = Tourism(place,numpeople,numdays,chargeperday)
   total = tour.cal_cost(numpeople,numdays,chargeperday)
   tour.display()
except InvalidInputError as e:
   print(e.msg)
