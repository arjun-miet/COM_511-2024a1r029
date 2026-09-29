"""Wap to show that tuple values cant be changed directly. convert tuple into list , update it and convert it back into tuple"""

tup = ("Hi" , "Sister")
print("Original Tuple: " ,tup)
lst = []
for i in tup:
    lst.append(i)

lst[0]="Hello"

tup2=tuple(lst)

print("Converted and Updated Tuple: ",tup2)
