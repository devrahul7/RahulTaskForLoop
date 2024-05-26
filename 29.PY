# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"]
# expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']

a = ['ram', 'shyam']

new_lst = []

for i in a:
    new_lst.append("Dr."+i)

for i in range(1,len(a)+1):
    new_lst.append("Dr.{}".format(i))

print(new_lst)
