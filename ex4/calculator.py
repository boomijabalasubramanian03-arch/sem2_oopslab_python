n1 = int(input("ENTER THE FIRST NUMBER:"))
n2 = int(input("ENTER THE SECOND NUMBER:"))
print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.FLOOR DIVISION")
def add(num1,num2):
   res1 = num1+num2
   return res1
def sub(num1,num2):
   res2 = num1-num2
   return res2
def mul(num1,num2):
   res3 = num1*num2
   return res3
def div(num1,num2):
   res4 = num1/num2
   return res4
def floordiv(num1,num2):
   res5 = num1//num2
   return res5
while True:
   choice = int(input("ENTER YOUR CHOICE:"))
   if choice == 1:
      print("ADDITION OF TWO NUMBERS IS:",add(n1,n2))
   elif choice == 2:
      print("SUBTRACTION OF TWO NUMBERS IS:",sub(n1,n2))
   elif choice==3:
      print("PRODUCT OF TWO NUMBERS IS:",mul(n1,n2))
   elif choice==4:
      print("DIVISION OF TWO NUMBERS IS:",div(n1,n2))
   elif choice==5:
      print("FLOOR DIVISION OF TWO NUMBERS IS:",floordiv(n1,n2))
   else:
      print("INVALID CHOICE")
      break
