name=input("Enter your name:")
found=False
with open("students.txt","r") as f:
    for line in f:
        if name in line:
            print(line)
            found=True
            break
if not found:
    print("Student not found")