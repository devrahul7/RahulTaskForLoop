# 11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]

lst = [1,2,3,4]
new_list = []
for i in lst: 
    if i == 1:
        new_list.append(i)
        new_list.append("a")
        new_list.append(2)
        new_list.append(4)    
print(new_list)
    
