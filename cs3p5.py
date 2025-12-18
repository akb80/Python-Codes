import csv
total=0
with open("sales.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total+=int(row["Price"])
print(total)