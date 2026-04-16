class Scientist:
  def __init__(self,name):
    self.name = name
  def display(self):
    print("NAME OF THE PERSON :",self.name)
  class Info:
    def __init__(self,height,weight,colour):
      self.height = height
      self.weight = weight
      self.colour = colour
    def display(self):
      print("HEIGHT OF THE PERSON :",self.height)
      print("WEIGHT OF THE PERSON :",self.weight)
      print("COLOUR OF THE PERSIN :",self.colour)
name = input("ENTER NAME :")
S = Scientist(name)
height = float(input("ENTER HEIGHT:"))
weight = float(input("ENTER WEIGHT:"))
colour = input("ENTER COLOUR:")
I = S.Info(height,weight,colour)
S.display()
I.display()
