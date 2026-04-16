try:
   num1 = int(input("ENTER NUMBER 1:"))
   num2 =int(input("ENTER NUMBER 2:"))
   num3 = input("ENTER THE NUMBER:")
   print(num1/num2)
   if num3.isdigit():
      print(num1-int(num3))
   else:
      print(num1-num3)
   l = eval(input("ENTER THE LIST ELEMENTS:"))
   print(l[2])
   print(n3)
except ZeroDivisionError:
   print("DIVIDE BY ZERO ERROR!")
except ValueError:
   print("INVALID INPUT!")
except TypeError:
   print("UNSUPPORTED OPERAND!")
except NameError:
   print("UNDEFINED VARIABLE!")
try:
   k=0
   l = eval(input("ENTER THE LIST ELEMENTS:"))
   for h in range(len(l)+1):
     print(h,":",l[h])
     k += 1
except IndexError:
   print(k,"INDEX OUT OF RANGE!")
try:
   iterator = iter(l)
   for i in range(len(l)+1):
     print(next(iterator))
except StopIteration:
   print("STOP ITERATION : ELEMENT NOT FOUND!")
