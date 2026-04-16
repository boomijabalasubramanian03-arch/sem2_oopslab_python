l1 = eval(input("ENTER THE FIRST LIST:"))
l2 = eval(input("ENTER THE SECOND LIST:"))
s1 = set(l1)
s2 = set(l2)
print("1.USING UNION\n2.USING INTERSECTION\n3.FINDING DIFFERENCE\n4.FINDING SYMMETRIC DIFFERENCE")
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      print("THE ELEMENTS IN BOTH THE SETS ARE",s1.union(s2))
   elif ch==2:
      print("THE COMON ELEMENTS IN BOTH THE SETS ARE:",s1.intersection(s2))
   elif ch==3:
      print("THE DIFFERENCE BETWEEN BOTH THE SETS ARE ",s1.difference(s2))
   elif ch==4:
      print("THE SYMMETRIC DIFFERENCE BETWEEN BOTH THE SETS ARE",s1.symmetric_difference(s2))
   else:
      print("INVALID CHOICE")
      exit(0)
