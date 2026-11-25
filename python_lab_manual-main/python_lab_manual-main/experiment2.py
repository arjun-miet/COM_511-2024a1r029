# Program to illustrate iteration over a list and dictionary

# List
list = [10, 20, 30, 40, 50]

print("Iteration over List:")
for item in list:
    print(item)

# Dictionary
dictionary = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

print("\nIteration over Dictionary:")
for key, value in dictionary.items():
    print(key, ":", value)




#     low = 0
# high = len(sorted_data) - 1
# binary_index = -1

# while low <= high:
#     mid = (low + high) // 2

#     if sorted_data[mid] == target:
#         binary_index = mid
#         break
#     elif sorted_data[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1

# if binary_index == -1:
#     print(f"Target {target} not found using binary search")
# else:
#     print(f"Target {target} found at index {binary_index} in sorted list")

# print("Sorted list:", sorted_data)