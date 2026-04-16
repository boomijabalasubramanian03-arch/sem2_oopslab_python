n = int(input("ENTER THE NUMBER OF ELEMENTS:"))
l = [];p=1
for k in range(n):
   num = int(input("ENTER THE ELEMENT:"))
   l.append(num)
print("1.SECOND LARGEST ELEMENT\n2.PRODUCT OF ELEMENTS\n3.FREQUENCY")
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      for i in range(0,n):
         for j in range(i,n):
            if l[i]<l[j]:
             t = l[i]
             l[i]=l[j]
             l[j]=t
      print("THE SECOND LARGEST ELEMENT IS ",l[1])
   elif ch==2:
      for a in range(n):
         p = p*l[a]
      print("PRODUCT IS",p)
   elif ch==3:
      no = int(input("ENTER THE FREQUENCY:"))
      for ele in range(n):
         c = l.count(ele)
         if c==no:
          print("THE ELEMENT OCCURED IS",ele)
         else:
          continue
   else:
      print("INVALID CHOICE")
      exit(0)
