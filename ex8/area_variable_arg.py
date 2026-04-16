class Shape:
  def area(self,*args):
    if len(args)==1:
     radius = args[0]
     return 3.14*radius*radius
    elif len(args)==2:
     l = args[0]
     b  = args[1]
     return l*b
    elif len(args)==3:
     l = args[0]
     b = args[1]
     h = args[2]
     return 2*(l*b + b*h + h+l)
    else:
     print("NO DIMENSIONS PROVIDED!")
s = Shape()
print("=====MENU=====")
print("1.SURFACE AREA OF CUBOID\n2.AREA OF RECTANGLE\n3.AREA OF CIRCLE")
n = int(input("ENTER HOW MANY TIMES YOU ARE GONNA RUN THIS PROGRAM:"))
for i in range(n):
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   l = float(input("ENTER THE LENGTH :"))
   b = float(input("ENTER THE BREADTH :"))
   h = float(input("ENTER THE HEIGHT:"))
   print("SURFACE AREA OF THE CUBOID IS:",s.area(l,b,h))
  elif ch==2:
   l = float(input("ENTER THE LENGTH :"))
   b = float(input("ENTER THE BREADTH :"))
   print("AREA OF RECTANGLE IS :",s.area(l,b))
  elif ch==3:
   l = float(input("ENTER THE RADIUS:"))
   print("AREA OF THE CIRCLE:",s.area(l))
  else:
   s.area()
