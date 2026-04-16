def factor(n):
   l = []
   for i in range(1,n+1):
      if n%i==0:
       l.append(i)
   return l
def primefact(n):
   c=0
   l1 = [];l2=[]
   for i in range(2,n+1):
     if n%i==0:
      l1.append(i)
   for j in l1:
     for k in range(2,j):
       if j%k==0:
        c+=1
     if c==0:
      l2.append(j)
   return l2

from factors import *
num1 = int(input("ENTER THE NUMBER:"))
res1 = factor(num1)
print("THE FACTORS OF",num1,"ARE :")
for i in res1:
      print(i,end=' ')
print()

num2 = int(input("ENTER THE NUMBER:"))
res2 = primefact(num2)
print("THE PRIME FACTORS OF",num2,"ARE :")
for i in res2:
   print(i,end=' ')
print()
