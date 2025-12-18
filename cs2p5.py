import csv
emp_id=input("enter employee id:")
with open("attendance.csv","r") as f:
    reader = csv.DictReader(f)
    found=False
    for row in reader:
        if row["EmpId"]==emp_id:
            print(row)
            found=True
            break
        if not found:
            print("not found")