num = int(input("ENTER THE NUMBER:"))
temp = num;res=0
while num>0 :
   rem = num%10
   res += rem
   num//=10
if temp%res==0 :
   print(temp,"is a harshad number")
else:
   print(temp,"is not a harshad number")
