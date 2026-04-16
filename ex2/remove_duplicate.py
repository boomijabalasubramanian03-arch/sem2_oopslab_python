s1 = input("ENTER THE STRING:")
l = []
for i in s1:
   if i not in l:
      l.append(i)
print("THE RESULTANT STRING IS:","".join(l))
