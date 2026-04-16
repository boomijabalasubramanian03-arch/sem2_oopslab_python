def fibo(n):
   if n==0:
      return 0
   if n==1:
      return 1
   return fibo(n-1) + fibo(n-2)
r = int(input("ENTER THE LIMIT:"))
for i in range(r):
   print(fibo(i))
