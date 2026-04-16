unit = float(input("ENTER THE UNITS CONSUMED:"))
if unit<=100 :
   bill = unit*10
   print("THE NET BILL IS",bill)
elif unit>=101 and unit<=200 :
   bill = (100*10) + ((unit-100)*15)
   print("THE NET BILL IS",bill)
elif unit>=201 and unit<=300 :
   bill = (100*10)+(100*15)+((unit-200)*20)
   print("THE NET BILL IS",bill)
elif unit>300 :
   bill = (100*10)+(100*15)+(100*20)+((unit-300)*30)
   print("THE NET BILL IS",bill)
else :
   pass
