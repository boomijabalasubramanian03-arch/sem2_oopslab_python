s = input("ENTER THE STRING:")
r = ""
for i in s:
   if i>='a' and i<='z':
      r += chr(ord(i)-32)
   else:
      r+=i
print("THE RESULTANT STRING IS :",r)
