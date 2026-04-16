import csv
with open("emp.csv","w",newline='') as f:
   w=csv.writer(f)
   w.writerow(["ENO","ENAME","ESAL","EDDR"])
   n=int(input("ENTER NO OF EMPLOYEES:"))
   for i in range(n):
      eno=input("ENTER EMLPOYEE NUMBER:")
      ename=input("ENTER EMPLOYEE NAME:")
      esal=input("ENTER EMPLOYEE SALARY:")
      ed=input("ENTER EMPLOYEE ADDRESS:")
      w.writerow([eno,ename,esal,ed])
print("WRITTEN SUCCESSFULLY!")
with open("emp.csv","r") as f:
   r=csv.reader(f)
   n=next(r)
   maxi=0
   top=[]
   for row in r:
     s=float(row[2])
     if s>maxi:
      maxi=s
      top=row
   if top:
    print("DETAILS OF EMPLOYEE WITH HIGH SALARY")
    print("EMPLOYEE NO:",top[0])
    print("EMPLOYEE NAME:",top[1])
    print("EMPLOYEE SALARY:",top[2])
    print("EMPLOYEE ADDRESS:",top[3])
   else:
    print("NO VALID DATA FOUND!")
