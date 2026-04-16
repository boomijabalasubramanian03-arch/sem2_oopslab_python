num = input("ENTER THE NUMBER:")
l = len(num)
n = int(num)
temp = n;arm=0
while n>0 :
   rem = n%10
   arm += rem**l
   n//=10
if temp==arm :
   print (temp,"is an armstrong number")
else :
   print(temp,"is not an armstrong number")
