""" WAP to input marks of 10 stduents . store only valid marks between 0 and 100 in a list , skip invalid marks """

n = list(map(int , input("Enter marks of 10 students: ").split()))
lst=[]
for i in n:
    if 0 <= i <=100:
        lst.append(i)

for i in lst:
    print(i)