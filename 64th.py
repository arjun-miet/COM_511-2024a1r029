"""WAP to check whether a given value is present in a tuple . if yes , then display its position"""

tup =(1,2,3,4,5,6)
target=int(input("Enter target value: "))
found = False
for i in tup:
    if tup[i]==target:
        print(f"present at position {i}")
        found = True
        break
if not found:
    print("Target not found")