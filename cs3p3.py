import csv
with open("sales.txt", "r") as txt, open("sales.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["PID", "PName", "Price"])
    for i in txt:
        writer.writerow(i.strip().split(","))
