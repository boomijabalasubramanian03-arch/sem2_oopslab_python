s = input("ENTER THE STRING:")
l = s.split()
l1 = []
i = len(l)-1
while i>=0:
   l1.append(l[i][::-1])
   i -= 1
print("RESULTANT STRING IS :"," ".join(l1))
