def gpa(no,stud):
   l = []
   s1 = {}
   s1[0] = 3
   s1[1] = 4
   s1[2] = 3
   for k in range(0,no):
    val = list(stud.values())
    gd = {}
    res = 0
    for c in range(3):
     for v in range(len(val)):
      if val[v][1][c]=="O":
       gd[c] = 10
      elif val[v][1][c]=="A+":
       gd[c] = 9
      elif val[v][1][c]=="A":
       gd[c]=8
      elif val[v][1][c]=="B+":
       gd[c]=7
      elif val[v][1][c]=="B":
       gd[c]=6
      else:
       gd[c]=0
       print("REAPPERA")
     res = res + (s1[c]*gd[k])
    l.append(res/10)
   l.sort(reverse=True)
   rank={}
   for i in range(0,len(l)):
    rank[l[i]] = i+1
   return rank
no = int(input("ENTER NO OF STUDENTS:"))
stud={}
for o in range(no):
 name = input("ENTER STUDENT NAME:")
 rn = int(input("ENTER ROLL NUMBER:"))
 gr = eval(input("ENTER GRADES:"))
 stud[rn] = [name,gr]
z = gpa(no,stud)
ans1=[]
x =list(stud.values())
for m in range(len(x)):
   ans1.append(x[m][0])
y = list(z.keys())
v = list(z.values())
print("NAME\tGPA\tRANK")
for n in range(len(ans1)):
   print(ans1[n],"\t",y[n],"\t",v[n])
