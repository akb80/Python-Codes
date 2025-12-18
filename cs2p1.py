import csv
with open("attendance.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["EmpId","Name","Date","Status"])
    writer.writerow(["123","John","19","present"])
    writer.writerow(["124","abhi","20","absent"])
    writer.writerow(["125","sita","19","present"])
print("attendance.csv created")