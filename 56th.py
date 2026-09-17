""" WAp to input a list of numbers and create a new list containing only unique elements"""

ls = list(map(int , input("Enter Numbers: ").split()))

lst = []

for i in ls:
    if i in lst:
        continue
    else:
        lst.append(i)

print(lst)