""" WAP to input numbers in a list and create two separate lists for even and odd numbers"""

num = list(map(int , input("Enter a list: ").split()))
even_no = []
odd_no = []
for i in num:
    if i%2==0:
        even_no.append(i)
    else:
        odd_no.append(i)

#Display the final lists
print("Original List: ",num)
print("Even Numbers: ",even_no)
print("Odd Numbers: ",odd_no)