d = {}
n1 = int(input("ENTER NUMBER OF EMPLOYEES:"))
i = 1
while i<=n1:
   empid = int(input("ENTER EMPLOYEE ID:"))
   empname = input("ENTER EMPLOYEE NAME:")
   empsal = int(input("ENTER EMPLOYEE SALARY:"))
   d[empid] = [empname,empsal]
   i += 1
print("EMP ID \t EMP NAME \t EMP SALARY")
for emp in d:
   if d[emp][1] >= 50000:
      print(emp,'\t',d[emp][0],'\t\t',d[emp][1])
