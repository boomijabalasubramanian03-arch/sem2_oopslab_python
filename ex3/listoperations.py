l = eval(input("ENTER THE LIST ELEMENTS:"))
print("1.LENGTH OF THE GIVEN LIST\n2.COUNTING OCCURANCE\n3.FINDING INDEX\n4.MINIMUM ELEMENT\n5.MAXIMUM ELEMENT")
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      print("LENGTH OF THE LIST IS",len(l))
   elif ch==2:
      k = int(input("ENTER THE ELEMENT:"))
      co = l.count(k)
      print("THE ELEMENT",k,"OCCURED",co,"TIMES")
   elif ch==3:
      m = int(input("ENTER THE ELEMENT:"))
      print("THE INDEX OF",m,"IS",l.index(m))
   elif ch==4:
      print("THE MINIMUM ELEMENT IS",min(l))
   elif ch==5:
      print("THE MAXIMUM ELEMENT IS",max(l))
   else:
      print("INVALID CHOICE")
      exit(0)

