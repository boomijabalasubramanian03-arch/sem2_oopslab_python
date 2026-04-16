class person:
 def __init__(self,name):
   self.name = name
 def display_name(self):
   print("NAME OF THE STUDENT IS",self.name)
class student(person):
  def __init__(self,name,stid,l):
    super().__init__(name)
    self.stid = stid
    self.marks = l
    self.tot = 0
  def tot_calc(self):
    for k in range(len(self.marks)):
      self.tot += self.marks[k]
    return self.tot
  def avg_calc(self):
    return self.tot/len(self.marks)
  def display(self):
    self.tot_calc()
    self.avg_calc()
    self.display_name()
    print("STUDENT ID IS ",self.stid)
    print("TOTAL MARK IS ",self.tot)
    print("AVERAGE MARK IS ",self.avg_calc())
l = []
name = input("ENTER THE STUDENT NAME:")
stid = int(input("ENTER THE STUDENT ID:"))
n = int(input("ENTER NO OF SUBJECTS:"))
for i in range(n):
   m = int(input("ENTER THE MARK 1:"))
   l.append(m)
obj = student(name,stid,l)
obj.display()
