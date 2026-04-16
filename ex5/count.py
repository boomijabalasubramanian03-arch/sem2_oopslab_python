class Count:
   c = 0
   def __init__(self):
      Count.c = Count.c+1
   @classmethod
   def display(cls):
      print("NO OF OBJECTS CREATED:",cls.c)
a1 = Count()
a2 = Count()
Count.display()
a3 = Count()
a4 = Count()
Count.display()
