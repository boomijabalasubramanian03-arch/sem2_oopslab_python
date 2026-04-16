n = input("ENTER THE PASSWORD:")
u = 0
sc = '!@#$%^&*()_+-='
if len(n)>=8:
   for i in n:
      if i.isupper()or i.islower()or i.isdigit()or i in sc:
       u+=1
      else:
       break
if u>=8:
   print("Valid password")
else:
   print("Invalid password")
