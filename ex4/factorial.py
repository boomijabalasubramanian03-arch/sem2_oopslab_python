def fact(n):
   r = 1
   while n>=1:
      r = r*n
      n = n-1
   return r
num = int(input("ENTER THE RANGE:"))
for i in range(1,num+1):
   print("FACTORIAL OF",i,":",fact(i))
