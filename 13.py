# 13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

lst = [1,2,3,"d",4,5,"a"]
new_list1 = []
new_list2 = []
for i in lst:
    if isinstance(i,str):
        new_list1.append(i)
    else:
        new_list2.append(i)
print(new_list1,new_list2)
    