n = int(input("ENTER THE NUMBER:"))
for i in range(1,n+1):
   if i%3==0:
      print(i,": XYZ")
   if i%5==0:
      print(i,": ABC")
   if i%3==0 and i%5==0:
      print(i,": XYZABC")
