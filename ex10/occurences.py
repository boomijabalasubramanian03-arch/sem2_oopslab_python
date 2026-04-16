content = input("ENTER THE CONTENT OF THE FILE TO WRITE:")
with open("file.txt","w") as f:
   f.write(content)
def count(wo):
   with open("file.txt","r") as char:
      words = char.read().lower().split()
      count = 0
      for word in words:
         if word.find(wo)==0 and len(word)==len(wo):
            count+=1
      print("The word",wo,"occured",count,"times in the file")
wo = input("ENTER THE WORD TO FIND OCCURENCE:")
count(wo)
