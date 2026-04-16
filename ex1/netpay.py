BP = float(input("ENTER THE BASIC PAY OF AN EMPLOYEE:"))
G = input("ENTER THE GRADE VALUE:")
DA = 0.2*BP
HRA = 0.5*BP
PF = 0.11*BP
if G in "aA":
   A = 1700
   NP = BP+DA+HRA+A-PF
   print("NET PAY OF THE EMPLOYEE IS :",NP)
elif G in "bB":
   A = 1500
   NP = BP+DA+HRA+A-PF
   print("NET PAY OF THE EMPLOYEE IS :",NP)
elif G in "cC" :
   A = 1000
   NP = BP+DA+HRA+A-PF
   print("NET PAY OF THE EMPLOYEE IS :",NP)
else :
   print ("INVALID INPUT")
