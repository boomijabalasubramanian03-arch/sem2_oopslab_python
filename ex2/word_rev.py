s = input("ENTER THE STRING:")
l = s.split();l1=[]
i = len(l)-1
while i>=0 :
   l1.append(l[i])
   i -= 1
opt = " ".join(l1)
print("REVERSED STRING IS :",opt)
