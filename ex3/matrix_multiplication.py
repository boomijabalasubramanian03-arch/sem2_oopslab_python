r = int(input("ENTER NO OF ROWS:"))
c = int(input("ENTER NO OF COLUMNS:"))
A = []
print("ENTER THE ELEMENTS OF A:")
for i in range(r):
   row=[]
   for j in range(c):
     v = int(input("ELEMENT :"))
     row.append(v)
   A.append(row)
B = []
print("ENTER ELEMENTS OF MATRIX B:")
for a in range(r):
   row1 = []
   for b in range(c):
     v1 = int(input("ELEMENT:"))
     row1.append(v1)
   B.append(row1)
C=[]
for l in range(r):
   Ans = []
   for p in range(c):
     v1 = 0
     for k in range(c):
       v1 += A[l][k]*B[k][p]
     Ans.append(v1)
   C.append(Ans)
print("MATRIX MULTIPLICATION")
print(C)
