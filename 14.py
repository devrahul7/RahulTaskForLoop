# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

lst = [1,2,3,4,"a","b"]
intlist = []
strlist = []

for i in lst:
    if isinstance(i,str):
        strlist.append(i)
    else:
        intlist.append(i)
    
print(strlist)
print(intlist)
   