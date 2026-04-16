num = int(input("ENTER THE NUMBER OF STUDENT:"))
d = {}
for i in range(num):
   name = input("ENTER NAME OF STUDENT:")
   mark = float(input("ENTER THE MARK SCORED:"))
   d[name] = mark
while True:
   n = input("ENTER NAME TO FIND MARKS:")
   m = d.get(n,-1)
   if m==-1:
      print("INFORMATION NOT FOUND")
   else:
      print(n,"==>",m)
   opt = input("DO YOU WANT TO CONTINUE: YES OR NO :")
   if opt == "NO":
      break
print("THANK YOU")
