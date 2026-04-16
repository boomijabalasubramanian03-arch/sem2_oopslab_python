import csv
f=open("emp.csv","r")
r=csv.reader(f)
d=list(r)
for l in d:
   for w in l:
      print(w,"\t",end='')
   print()
