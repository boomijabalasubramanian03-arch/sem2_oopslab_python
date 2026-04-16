s = input("ENTER THE STRING:")
n1=n2=r=""
for i in s:
   if i.isalpha() :
      n1+=i
   else:
      n2+=i
for j in sorted(n1):
   r += j
for k in sorted(n2):
   r += k
print("THE SORTED STRING IS :",r)
