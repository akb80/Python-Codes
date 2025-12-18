def common(list1,list2):
    res=[]
    for i in list1:
        if i in list2 and i not in res:
            res.append(i)
    print(res)
print(common([1,2,3,4,5],[3,4,5,6,7]))