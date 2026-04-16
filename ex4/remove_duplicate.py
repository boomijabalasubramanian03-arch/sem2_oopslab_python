def duplicate(s):
   l = []
   for i in range(0,len(s)-1):
      if s[i] != s[i+1]:
       l.append(s[i])
   l.append(s[-1])
   res = "".join(l)
   return res
str1 = input("ENTER THE STRING:")
print("THE MODIFIED STRING IS:",duplicate(str1))
