s1 = input("ENTER THE STRING:")
l = s1.split()
l1 = []
i = 0
while i<len(l):
   if i%2==0:
      l1.append(l[i])
   else:
      l1.append(l[i][::-1]
   i+=1
opt = ''.join(l1)
print("Actual string:",s1)
print("Generated string:",opt)
