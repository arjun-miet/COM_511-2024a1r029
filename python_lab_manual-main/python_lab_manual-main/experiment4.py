# Program to convert temperature between Celsius and Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Celsius:", celsius)




































































# ```python
# n = int(input())

# expenses = {}
# total = 0

# for i in range(n):
#     category, amount = input().split()
#     category = category.lower()
#     amount = float(amount)

#     expenses[category] = expenses.get(category, 0) + amount
#     total += amount

# sorted_expenses = sorted(expenses.items(), key=lambda x: (-x[1], x[0]))

# print(f"Total Monthly Expense: {total:.2f}")
# print("Expenses by Category:")

# for category, amount in sorted_expenses:
#     print(f"{category} : {amount:.2f}")

# highest_category, highest_amount = sorted_expenses[0]

# print(f"Highest Expense Category: {highest_category}")
# print(f"Highest Expense Amount: {highest_amount:.2f}")
# ```
