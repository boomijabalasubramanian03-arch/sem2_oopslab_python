import os,sys
fn=input("ENTER FILE NAME:")
if os.path.isfile(fn):
   print("FILE",fn,"EXISTS")
   f=open(fn,"r")
else:
   print("FILE DOESNOT EXIST!",fn)
   sys.exit(0)
lc=wc=cc=0
for l in f:
  lc=lc+1
  cc=cc+len(l)
  w=l.split()
  wc=wc+len(w)
print("NUMBER OF LINES IN THE FILE:",lc)
print("NUMBER OF WORDS IN THE FILE:",wc)
print("NUMBER OF CHARACTERS IN THE FILE:",cc)
