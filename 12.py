# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.

lst= [1,2,3,4,5]
odd = []
even = []
for i in lst:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print(even)
print(odd)