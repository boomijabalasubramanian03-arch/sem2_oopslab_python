n = input("ENTER THE STRING:")
opt = ''
for i in n:
   if i.isalpha():
      opt = opt+i
      p=i
   else:
      opt = opt + p*(int(i)-1)
print(opt)
