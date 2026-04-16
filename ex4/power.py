def power(n,a):
   if a==1:
      return n
   else:
      return n*power(n,a-1)
base = int(input("ENTER THE BASE VALUE:"))
exp = int(input("ENTER THE EXPONENT VALUE:"))
i = power(base,exp)
print("THE VALUE OF",base,"TO THE POWER",exp,"is",i)
