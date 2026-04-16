import sys
import gc
class User:
  def __init__(self,name,job_title):
    self.name = name
    self.job_title  = job_title
    self.connections = []
  def add_connection(self,connection_name):
    if connection_name not in self.connections:
     self.connections.append(connection_name)
     print(self.name,"IS CONNECTED WITH",connection_name)
    else:
     print(self.name,"IS ALREADY CONNECTED WITH",connection_name)
  def remove_connection(self,connection_name):
    if connection_name in self.connections:
     self.connections.remove(connection_name)
     print(self.name,"REMOVED CONNECTION WITH",connection_name)
    else:
     print("NO CONNECTION NAMED",connection_name,"FOUND FOR",self.name)
  def view_connections(self):
    print(self.name,"'s CONNECTIONS :")
    if not self.connections:
     print("NO CONNECTIONS")
    else:
     for i in self.connections:
      print("",i)
  def show_ref_count(self):
    print("REFERENCE COUNT FOR",self.name,":",sys.getrefcount(self))
name = input("ENTER YOUR NAME:")
job_title = input("ENTER YOUR JOB TITLE:")
gc.enable()
user = User(name,job_title)
while True:
  print("MENU")
  print("1.ADD CONNECTION\n2.REMOVE CONNECTION\n3.VIEW CONNECTION\n4.SHOW REFERENCE\n5.EXIT")
  ch = int(input("ENTER YOUR CHOICE(1-5):"))
  if ch==1:
   connection_name = input("ENTER THE NAME OF THE PERSON YOU WANT TO CONNECT WITH:")
   user.add_connection(connection_name)
  elif ch==2:
   connection_name = input("ENTER THE NAME YOU WANT TO DISCONNECT WITH:")
   user.remove_connection(connection_name)
  elif ch==3:
   user.view_connections()
  elif ch==4:
   user.show_ref_count()
  elif ch==5:
   print("EXITING...")
   user.show_ref_count()
   del user
   gc.collect()
   break
  else:
   print("INVAID CHOICE!")
