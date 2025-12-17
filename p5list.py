import copy
org=[[1,2,3],[4,5,6],[7,8,9]]
shallow=copy.copy(org)
deep=copy.copy(org)
print(org)
print(shallow)
print(deep)
org[0][0]=99
print(org)
print(shallow)
print(deep)