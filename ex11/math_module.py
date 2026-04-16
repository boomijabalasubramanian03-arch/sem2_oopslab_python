import math
print("=====MENU=====")
print("1.FINDING SQUAREROOT\n2.FINDING POWER\n3.DEGREE-RADIAN")
print("4.LOG VALUE\n5.ROUNDING\n6.FACTORIAL\n7.COMPOUND INTEREST\n")
while True:
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   num = int(input("ENTER THE NUMBER TO FIND SQUAREROOT:"))
   print("SQUAREROOT OF",num,"IS",math.sqrt(num))
  elif ch==2:
   base = int(input("ENTER THE BASE VALUE:"))
   exp = int(input("ENTER THE EXPONENT VALUE:"))
   print("THE VALUE OF",base,"TO THE POWER OF",exp,"IS:",math.pow(base,exp))
  elif ch==3:
   angle = float(input("ENTER THE ANGLE VALUE:"))
   print("SIN VALUE OF",angle,"IS:",math.sin(angle))
   print("COS VALUE OF",angle,"IS:",math.cos(angle))
   print("TAN VALUE OF",angle,"IS:",math.tan(angle))
  elif ch==4:
   n1 = int(input("ENTER THE NUMBER:"))
   print("NATURAL LOG OF",n1,"IS:",math.log(n1))
   print("BASE 10 LOG OF 1000:",math.log10(n1))
  elif ch==5:
   num = float(input("ENTER THE FLOAT VALUE:"))
   print("ROUNDED VALUE:",round(num))
   print("FLOOR VALUE OF",num,"IS:",math.floor(num))
   print("CEIL VALUE OF",num,"IS:",math.ceil(num))
  elif ch==6:
   num = int(input("ENTER THE NUMBER:"))
   r = int(input("ENTER NO OF TIMES:"))
   permutations = math.factorial(num)/math.factorial(num-5)
   print("PERMUTAIONS OF",num,"ITEMS TAKEN",r,"AT A TIME:",int(permutations))
  elif ch==7:
   p = float(input("ENTER THE AMOUNT:"))
   rate = float(input("ENTER RATE OF INTEREST:"))
   time = int(input("ENTER THE TIME PERIOD:"))
   A = p*math.pow((1+rate),time)
   print("COMPOUND AMOUNT AFTER",time,"YEARS AT",rate,"% INTEREST:Rs",A)
  elif ch==8:
   print("EXITING!")
   break
  else:
   print("INVALID CHOICE!")
   exit(0)
  choice = input("DO YOU WANT TO CONTINUE(Y/N):")
  if choice=="Y":
   continue
  else:
   print("THANK YOU!")
   break
