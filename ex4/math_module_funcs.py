from math import *
print("1.FINDING SQUARE ROOT\n2.USING FLOOR FUNCTION\n3.USING CEIL FUNCTION\n4.FINDING LOG")
print("5.FINDING SIN\n6.FINDING COS\n7.FINDING TAN\n8.FINDING FABS")
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      num = int(input("ENTER THE NUMBER:"))
      print("THE SQUARE ROOT OF",num,"IS",sqrt(num))
   elif ch==2:
      num = float(input("ENTER THE NUMBER:"))
      print("THE FLOOR VALUE OF",num,"IS",floor(num))
   elif ch==3:
      num = float(input("ENTER THE NUMBER:"))
      print("THE CEIL VALUE OF",num,"IS",ceil(num))
   elif ch==4:
      num = int(input("ENTER THE NUMBER:"))
      print("THE LOG VALUE OF",num,"IS",log(num))
   elif ch==5:
      num = int(input("ENTER THE NUMBER:"))
      print("THE SIN VALUE OF",num,"IS",sin(num))
   elif ch==6:
      num = int(input("ENTER THE NUMBER:"))
      print("THE COS VALUE OF",num,"IS",cos(num))
   elif ch==7:
      num = int(input("ENTER THE NUMBER:"))
      print("THE TAN VALUE OF",num,"IS",tan(num))
   elif ch==8:
      num = float(input("ENTER THE NUMBER:"))
      print("THE POSITIVE VALUE OF",num,"IS",fabs(num))
   else:
      print("END")
      exit(0)
