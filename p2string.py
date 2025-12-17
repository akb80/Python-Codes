s=input("Enter a string: ")
w= s.split()
res=[]
for i in w:
    res.append(i[::-1])
print(" ".join(res))