# python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit
num = int(input("Enter a number: "))
while num>=10:
    sum_digits=0
    while num>0:
        digit=num%10
        sum_digits=sum_digits+digit
        num=num//10
        num=sum_digits
print("Single digit result: ",num)