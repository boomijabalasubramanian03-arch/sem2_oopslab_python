d = {}
n = int(input("ENTER NUMBER OF RECORDS:"))
for i in range(n):
   rn = int(input("ENTER STUDENT ROLL NUMBER:"))
   nm = input("ENTER STUDENT NAME:")
   d[rn] = nm
print("1.FINDING LENGTH\n2.TO GET VALUE BY PASSING KEY\n3.TO DELETE A RECORD\n 4.TO PRINT KEYS\n5.TO PRINT VALUES")
print("6.TO PRINT ITEMS\n7.TO COPY A RECORD\n8.TO UPDATE THE DICTIONARY")
while True:
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      print("LENGTH OF THE DICTIONARY IS",len(d))
   elif ch==2:
      key = int(input("ENTER THE KEY TO FIND:"))
      print("THE VALUE IS",d.get(key))
   elif ch==3:
      key = int(input("ENTER KEY TO DELETE:"))
      print("THE DELETED KEY IS",d.pop(key))
   elif ch==4:
      k = d.keys()
      for i in k:
       print("THE KEYS ARE",i)
   elif ch==5:
      v = d.values()
      for i in v:
       print("THE VALUES ARE",i)
   elif ch==6:
      print("THE ITEMS ARE :")
      for i,j in d.items():
       print(i,"==>",j)
   elif ch==7:
      p = d.copy()
      print("THE DICTIONARY AFTER COPYING IS",p)
   elif ch==8:
      key = int(input("ENTER ROLL NUMBER:"))
      value = input("ENTER NAME:")
      d.update({key:value})
      print("AFTER UPDATION",d)
   else:
      print("INVALID CHOICE")
      break
