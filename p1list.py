num=[1,2,3,2,4,1,5]
newNum=[]
for i in num:
    if i not in newNum:
        newNum.append(i)

print(newNum)