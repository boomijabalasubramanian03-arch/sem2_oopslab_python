from random import *
print("1.USING RANDOM\n2.USING RANDINT\n3.USING UNIFORM\n4.USING RANDRANGE\n5.USING CHOICE")
n = int(input("ENTER THE RANGE:"))
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      for j in range(n):
       print(random())
   elif ch==2:
      for j in range(n):
        print(randint(0,n))
   elif ch==3:
      for j in range(n):
       print(uniform(0,n))
   elif ch==4:
      for j in range(n):
       print(randrange(0,n))
   elif ch==5:
      l = eval(input("ENTER THE LIST:"))
      for j in range(n):
       print(choice(l))
   else:
      print("INVALID CHOICE")
      exit(0)
