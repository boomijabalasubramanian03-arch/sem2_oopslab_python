def bill(cus,ordno,d,delv,tax=5,**items):
   price = sum(items.values())
   tax1 = price*0.05
   dis = price*(d/100)
   bill = (price + tax1 + delv)-dis
   print("CUSTOMER NAME:",cus)
   print("ORDER NO:",ordno)
   print("DISCOUNT:",d,"%")
   print("TAX:",tax,"%")
   print("ITEMS AND PRICES:",items)
   print("DELIVERY CHARGE:",delv)
   return bill
cusnm = input("ENTER THE CUSTOMER NAME:")
ordnum = int(input("ENTER THE ORDER NUMBER:"))
d = int(input("ENTER THE DISCOUNT:"))
no =int(input("ENTER NO OF ITEMS:"))
items = {}
for i in range(no):
   k = input("ENTER ITEMS:")
   j = int(input("ENTER PRICE:"))
   items[k] = j
delv = int(input("ENTER DELIVERY CHARGE:"))
print("TOTAL BILL AMOUNT IS",bill(cusnm,ordnum,d,delv,tax=5,**items))
