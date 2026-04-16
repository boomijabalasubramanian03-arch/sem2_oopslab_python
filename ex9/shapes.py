class Shape:
  def area(self):
    return 0.0
class Circle(Shape):
  def __init__(self,r):
    self.r = r
  def area(self):
    return 3.14*self.r*self.r
class Rectangle(Shape):
  def __init__(self,l,b):
    self.l = l
    self.b = b
  def area(self):
    return self.l*self.b
class Triangle(Shape):
  def __init__(self,b,h):
    self.b = b
    self.h = h
  def area(self):
    return 0.5*self.b*self.h
print("AREA CALCULATION OF DIFFERENT SHAPES")
print("1.AREA OF CIRCLE\n2.AREA OF RECTANGLE\n3.AREA OF TRIANGLE")
while True:
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   r = float(input("ENTER THE RADIUS:"))
   c = Circle(r)
   print("AREA OF CIRCLE IS:",c.area())
  elif ch==2:
   l = float(input("ENTER THE LENGTH:"))
   b = float(input("ENTER THE BREADTH:"))
   r = Rectangle(l,b)
   print("AREA OF RECTANGLE:",r.area())
  elif ch==3:
   b = float(input("ENTER THE BASE VALUE:"))
   h = float(input("ENTER THE HEIGHT VALUE:"))
   t = Triangle(b,h)
   print("AREA OF TRIANGLE IS",t.area())
  else:
   print("INVALID CHOICE!")
  choice = input("DO YOU WANNA CONTINUE(Y/N():")
  if choice=="Y":
   continue
  else:
   print("END!")
   break
