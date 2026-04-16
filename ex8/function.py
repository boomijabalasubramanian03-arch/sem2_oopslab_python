class First:
  def fun(self):
    print("FIRST!")
class Second:
  def fun(self):
    print("SECOND!")
class Third:
  def fun(self):
    print("THIRD!")
class Fourth(First,Second):
  def fun(self):
    print("FOURTH!")
class Fifth(Second,Third):
  def fun(self):
    print("FIFTH!")
class Sixth(Fourth,Fifth,Third):
  def fun(self):
    print("SIXTH!")
s = Sixth()
s.fun()
a = Sixth.mro()
for i in a:
  print(i)
