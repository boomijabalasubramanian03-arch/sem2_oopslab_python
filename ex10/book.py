import os
FILE = "bookdata.txt"
def write_book():
  with open (FILE,"w") as f:
    f.write("BOOK ID\tTITLE\tAUTHOR\tPRICE\n")
    n = int(input("ENTER NO OF RECORDS:"))
    for i in range(n):
      bid = input("ENTER BOOK ID:")
      name = input("ENTER TITLE :")
      author = input("ENTER AUTHOR NAME:")
      price = float(input("ENTER PRICE:"))
      f.writelines([bid,"\t",name,"\t",author,"\t",str(price),"\n"])
    print("BOOKS WRITTEN SUCCESSFULLY!")
def read_book():
  if not os.path.isfile(FILE):
   print("FILE NOT EXIST!")
   return
  with open(FILE,"r") as f:
   print("CURRENT POSITION:",f.tell())
   content = f.read()
   print(content)
   print("FILE POINTER POSITION:",f.tell())
def seek_test():
  if not os.path.isfile(FILE):
   return
  with open(FILE,"r") as f:
   print(f.readline())
   print("CURRENT POSITION:",f.tell())
def check_file():
  if os.path.isfile(FILE):
   print("FILE EXIST!")
  else:
   print("FILE DOES NOT EXIST!")
def main():
  while True:
   print("=====MENU=====")
   print("1.TO WRITE\n2.TO READ\n3.TO USE SEEK\n4.TO CHECK FILE EXISTENCE\n5.EXIT")
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
    write_book()
   elif ch==2:
    read_book()
   elif ch==3:
    seek_test()
   elif ch==4:
    check_file()
   elif ch==5:
    print("END!")
    break
   else:
    print("INVALID CHOICE!")
main()
