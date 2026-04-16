w = input("ENTER THE WORD:")
l = []
for ch in w:
   if ch in "AEIOUaeiou":
      l.append(ch)
s = set(l)
print(s)
