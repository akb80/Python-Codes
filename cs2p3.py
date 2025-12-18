import csv
with open("attendance.csv","a",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["126","Ram","21","Absent"])
print("Record added")