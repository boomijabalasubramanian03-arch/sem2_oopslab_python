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
print("ELEMENTE OF MATRIX B:")
B = []
for a in range(0,r):
   row1 = []
   for b in range(0,c):
     v1 = int(input("ELEMENTS:"))
     row1.append(v1)
   B.append(row1)
C=[]
for k in range(r):
   Ans = []
   for t in range(c):
     A1=A[k][t]+B[k][t]
     Ans.append(A1)
   C.append(Ans)
print("MATRIX ADDITION")
print(C)
