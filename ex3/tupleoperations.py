l = eval(input("ENTER THE ELEMENTS:"))
n = tuple(l)
print("1.LENGTH OF TUPLE\n2.COUNT\n3.INDEX OF GIVEN ELEMENT\n4.SORTING TUPLE\n5.MINIMUM ELEMENT\n6.MAXIMUM ELEMENT")
while True:
   c = int(input("ENTER THE CHOICE:"))
   if c==1:
      print("LENGTH OF THE TUPLE IS",len(n))
   elif c==2:
      ele = int(input("ENTER THE ELEMENT:"))
      print("COUNT OF THE ELEMENT IS",n.count(ele))
   elif c==3:
      num = int(input("ENTER THE ELEMENT:"))
      print("INDEX OF THE ELEMENT IS",n.index(num))
   elif c==4:
      l1=tuple(sorted(n))
      print("THE SORTED TUPLE IS",l1)
   elif c==5:
      print("MINIMUM NUMBER IS",min(n))
   elif c==6:
      print("MAXIMUM NUMBER IS",max(n))
   else:
      print("INVALID CHOICE")
      exit(0)
