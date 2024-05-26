# 8 .given list is [1,2,3,4] but expected output in new list [2,3,4,5]

a =  [1,2,3,4]
new_list= []

for i in a:
    if i != 1:
        new_list.append(i)

new_list.append(5) 
 
print(f"old list: {a}")
print(f"new list: {new_list}")
        


