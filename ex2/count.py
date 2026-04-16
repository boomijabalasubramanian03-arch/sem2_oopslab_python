n = input("ENTER THE STRING:")
vow=cons=0
for i in n:
   if i in "AEIOUaeiou":
      vow+=1
   elif ord(i)>=65 and ord(i)<=122:
      cons+=1
   else:
      continue
print("NO OF VOWELS IS :",vow)
print("NO OF CONSONANTS IS:",cons)
