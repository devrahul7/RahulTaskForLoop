#33 Write a for loop which appends the type of each element in the first list to the second list.

lst = [5,6,"Mrrahul",3.0,True,1+1j]
newlst = []

for i in range(len(lst)):
    newlst.append(type(lst[i]))

print(f"Your list: {lst} \nConverted list is: {newlst}")