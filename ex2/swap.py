n = input("ENTER THE STRING:")
l = n.split()
if len(l)==2:
   s1 = l[0]
   s2=l[1]
   s3 = s2[0]+s1[1:]
   s4 = s1[0]+s2[1:]
   print(s3,s4)
else:
   print("INVALID INPUT")
