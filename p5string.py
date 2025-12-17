s="Python"
try:
    s[0]='j'
except TypeError as e:
    print("Error:",e)