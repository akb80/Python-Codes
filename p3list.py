num=[10,89,23,92,91,19]
largest=-1
secLargest=-1
for i in num:
    if i>largest:
        secLargest=largest
        largest=i
    elif i>secLargest and i!=largest:
        secLargest=i
print(secLargest)