class Shape:
  def area(self):
    return 0
  def display(self):
    print(self.__class__.__name__,"AREA:",self.area)
class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return 3.14*self.radius*self.radius
class Square(Shape):
  def __init__(self,side):
    self.side = side
  def area(self):
    return self.side*self.side
class Rectangle(Shape):
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth
  def area(self):
    return self.length*self.breadth
class Triangle(Shape):
  def __init__(self,base,height):
    self.base = base
    self.height = height
  def area(self):
    return 0.5*self.base*self.height
class Cuboid(Shape):
  def __init__(self,length,breadth,height):
    self.length = length
    self.breadth = breadth
    self.height = height
  def area(self):
    return 2*(self.length*self.breadth + self.breadth*self.height + self.length*self.height)
print("=====MENU=====")
print("1.AREA OF CIRCLE\n2.AREA OF SQUARE\n3.AREA OF RECTANGLE\n4.AREA OF TRIANGLE\n5.SURFACE AREA OF CUBOID")
while True:
  ch = int(input("ENTER YOUR CHOICE:"))
  if ch==1:
   radius = float(input("ENTER RADIUS:"))
   s1 = Circle(radius)
   print("AREA OF CIRCLE IS:",s1.area())
  elif ch==2:
   side = float(input("ENTER SIDE:"))
   s2 = Square(side)
   print("AREA OF THE SQUARE IS:",s2.area())
  elif ch==3:
   l = float(input("ENTER LENGTH:"))
   b = float(input("ENTER BREADTH:"))
   s3 = Rectangle(l,b)
   print("AREA OF THE RECTANGLE IS :",s3.area())
  elif ch==4:
   b = float(input("ENTER BASE:"))
   h = float(input("ENTER HEIGHT:"))
   s4 = Triangle(b,h)
   print("AREA OF THE TRINGLE IS:",s4.area())
  elif ch==5:
   l = float(input("ENTER LENGTH:"))
   b = float(input("ENTER BREADTH:"))
   h = float(input("ENTER HEIGHT:"))
   s5 = Cuboid(l,b,h)
   print("SURFACE AREA OF THE CUBOID IS:",s5.area())
  else:
   print("NO DIMENSIONS PROVIDED!")
  choice = input("DO YOU WANT TO CONTINUE(Y/N):")
  if choice=="Y":
   continue
  else:
   break
