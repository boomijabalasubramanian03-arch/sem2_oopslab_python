o = input("ENTER THE STRING:")
v = {'a','e','i','o','u'}
d = {}
for a in o:
  if a in v:
     d[a] = d.get(a,0)+1
for i,j in sorted(d.items()):
   print(i,"==>",j,"times")
