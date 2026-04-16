class Value_Error(Exception):
   def __init__(self,msg = "Value cannot be negative"):
      self.msg = msg
class messbill:
   def __init__(self,numdays,chargeperday):
      self.numdays = numdays
      self.chargeperday = chargeperday
   def validity(self,value):
     if value<0:
      raise Value_Error
   def calc_bill(self,numdays,chargeperday):
      self.validity(numdays)
      self.validity(chargeperday)
      total = self.numdays*self.chargeperday
      return total
try :
   numdays = int(input("ENTER NO OF  DAYS:"))
   chargeperday = float(input("ENTER CHARGE PER DAY:"))
   bill = messbill(numdays,chargeperday)
   total = bill.calc_bill(numdays,chargeperday)
   print(total)
except Value_Error as e:
   print(e.msg)
