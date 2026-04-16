from zipfile import *
f=ZipFile("f.zip","w",ZIP_DEFLATED)
f.write("f1.txt")
f.write("f2.txt")
f.write("f3.txt")
f.close()
print("f.zip CREATED SUCCESSFULLY!")
from zipfile import *
f=ZipFile("f.zip","r",ZIP_STORED)
n=f.namelist()
for n1 in n:
   print("FILE NAME:",n1)
   print("FILE CONTENT:")
   f1=open(n1,"r")
   print(f1.read())
   print()
