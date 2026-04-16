print("1.FINDING CUBES OF LIST ELEMENTS\n2.FINDING LENGTH\n3.FINDING FIRST LETTER FROM LIST OF WORDS")
while True:
   ch = int(input("ENTER YOUR CHIOCE:"))
   if ch==1:
      n = int(input("ENTER THE LIMIT:"))
      l = [x**3 for x in range(1,n+1)]
      print("THE CUBES ARE ",l)
   elif ch==2:
      s = input("ENTER THE STRING:").split()
      l = [[w.upper(),len(w)] for w in s]
      print(l)
   elif ch==3:
      s = eval(input("ENTER THE LIST OF STRINGS:"))
      l = [w[0] for w in s]
      print(l)
   else:
      print("INVALID CHOICE")
      exit(0)
