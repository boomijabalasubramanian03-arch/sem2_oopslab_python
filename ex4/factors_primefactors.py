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
