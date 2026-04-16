import gc
class Student:
  def __init__(self,name):
    self.name = name
    print("STUDENT:",self.name,"CREATED!")
  def __del__(self):
    print("STUDENT:",self.name,"DESTROYED!")
gc.enable()
name = input("ENTER NAME:")
s = Student(name)
print("CALLING GARBAGE COLLECTOR MANUALLY...")
gc.collect()
print("END OF THE PROGRAM!")
