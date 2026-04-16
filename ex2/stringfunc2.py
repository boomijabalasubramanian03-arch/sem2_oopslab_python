n = input("ENTER THE STRING:")
r = ''
for i in n:
   if i.isalpha() :
      r += i
      prev = i
   else:
      r += chr(ord(prev)+int(i))
print("THE RESULTANT STRING IS:",r)
