import csv
count=0
with open("attendance.csv",'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Status"]=="absent":
            count+=1
print("count:" ,count)