def char_count(s):
    count={}
    for i in s:
        count[i]=count.get(i,0)+1
    return count
print(char_count("hello"))