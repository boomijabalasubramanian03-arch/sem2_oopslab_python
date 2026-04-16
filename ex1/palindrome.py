num = int(input("ENTER THE NUMBER:"))
temp = num;rev=0
while num>0 :
   rem = num%10
   rev = rev*10 + rem
   num//=10
if temp==rev :
   print (temp,"is a palindrome")
else :
   print (temp,"is not a palindrome")
