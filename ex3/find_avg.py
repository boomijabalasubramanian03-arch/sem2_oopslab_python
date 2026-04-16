d = {}
tot = 0
n = int(input("ENTER THE NO OF SUBJECTS:"))
i = 1
while i<=n:
   sub = input("ENTER SUBJECT  NAME:")
   mark = float(input("ENTER MARKS SCORED:"))
   d[sub] = mark
   i += 1
print(d)
val = d.values()
l = len(val)
for i in d.values():
   tot += i
avg = tot/l
print("AVERAGE OF MARKS IS ",avg)
