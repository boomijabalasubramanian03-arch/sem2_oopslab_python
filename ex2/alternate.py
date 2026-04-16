s1 = input("ENTER THE STRING:")
s2 = input("ENTER THE STRING:")
r = ""
i=j=0
while i<len(s1) or j<len(s2) :
   if i<len(s1):
      r += s1[i]
      i+=1
   if j<len(s2):
      r += s2[j]
      j+=1
print("THE RESULTANT STRING IS :",r)
