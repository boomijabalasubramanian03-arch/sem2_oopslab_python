import numpy as np
print("=====MENU=====")
print("1.1D ARRAY OPERATIONS\n2.MATRIX OPERATIONS")
while True:
  ch = int(input("ENTER YOUR CHOICE(1D/2D):"))
  if ch==1:
   l = eval(input("ENTER THE LIST OF ELEMENTS:"))
   arr = np.array(l)
   print("1D ARRAY :",arr)
   print("====CHOICE====")
   print("1.ELEMENT WISE OPERATIONS\n2.MEAN\n3.STANDARD DEVIATION")
   while True:
     f = int(input("ENTER YOUR CHOICE:"))
     if f==1:
      num = int(input("ENTER NUMBER TO ADD TO EACH ELEMENT:"))
      print("ARRAY +",num,":",arr+num)
     elif f==2:
      print("MEAN:",np.mean(arr))
     elif f==3:
      print("STANDARD DEVIATION:",np.std(arr))
     else:
      print("INVALID CHOICE")
      break
  elif ch==2:
   r = int(input("ENTER NO OF ROWS:"))
   c = int(input("ENTER NO OF COLUMNS:"))
   A = []
   print("ELEMENTS OF MATRIX A")
   for i in range(0,r):
     row=[]
     for j in range(0,c):
       v = int(input("ELEMENTS:"))
       row.append(v)
     A.append(row)
   print("ELEMENTS OF MATRIX B")
   B = []
   for a in range(0,r):
     row1 = []
     for b in range(0,c):
       v1 = int(input("ELEMENTS:"))
       row1.append(v1)
     B.append(row1)
   K = np.array(A)
   L = np.array(B)
   print("MATRIX K:\n",K)
   print("MATRIX L:\n",L)
   print("1.MATRIX (+)\n2.MATRIX (-)\n3.MATRIX (*)\n4.TO FIND TRANSPOSE")
   while True:
     g = int(input("ENTER YOUR CHOICE:"))
     if g==1:
      print("K+L:\n",K+L)
     elif g==2:
      print("K-L:\n",K-L)
     elif g==3:
      print("K*L:\n",np.dot(K,L))
     elif g==4:
      print("TRANSPOSE OF MATRIX K:\n",K.T)
      print("TRANSPOSE OF MATRIX L:\n",L.T)
     else:
      break
  else:
   print("INVALID CHOICE:")
   break
