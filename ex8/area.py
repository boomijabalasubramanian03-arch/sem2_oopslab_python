class Shape:
  def area(self,l=None,b=None,h=None):
    if l is not None and b is not None and h is not None:
     print("SURFACE AREA OF CUBOID IS :",2*(l*b + b*h + h*l))
    elif l is not None and b is not None:
     print("AREA OF RECTANGLE IS :",l*b)
    elif l is not None:
     print("AREA OF SQUARE IS :",l*l)
    else:
     print("NO DIMENSIONS PROVIDED!")
s = Shape()
print("=====MENU=====")
print("1.SURFACE AREA OF CUBOID\n2.AREA OF RECTANGLE\n3.AREA OF SQUARE")
n = int(input("ENTER HOW MANY TIMES YOU ARE GONNA RUN THIS PROGRAM:"))
for i in range(n):
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   l = float(input("ENTER THE LENGTH :"))
   b = float(input("ENTER THE BREADTH :"))
   h = float(input("ENTER THE HEIGHT:"))
   s.area(l,b,h)
  elif ch==2:
   l = float(input("ENTER THE LENGTH :"))
   b = float(input("ENTER THE BREADTH :"))
   s.area(l,b)
  elif ch==3:
   l = float(input("ENTER THE LENGTH:"))
   s.area(l)
  else:
   s.area()
