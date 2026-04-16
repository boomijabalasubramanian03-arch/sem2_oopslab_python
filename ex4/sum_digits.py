def digit(n):
   e=0
   n1 = abs(n)
   while n1 != 0:
      s = n1%10
      e = e+s
      n1 = n1//10
   return e
num = int(input("ENTER THE NUMBER:"))
print("SUM OF DIGITS OF",num,"IS",digit(num))
