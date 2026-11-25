def max_of_three(a, b, c):
    return max(a, b, c)


def armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == n:
        return True
    else:
        return False


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number:", max_of_three(a, b, c))

n = int(input("Enter a number to check Armstrong: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")