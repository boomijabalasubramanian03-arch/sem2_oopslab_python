w = input("ENTER INPUT:")
d = {}
for a in w:
   d[a] = d.get(a,0)+1
for i,j in d.items():
   print(i,"==>",j,"times")
