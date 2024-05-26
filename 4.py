# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]


given_list = [1,"a","c",2,3,4]

for item in given_list:
  if isinstance(item,int):
    print(item)
