"""WAP to store repeated values in a tuple and count ho many times a given value appears"""
from collections import Counter
tup = (1,2,3,2,3,2,3,4,5,6,7,7)

counts = Counter(tup)

rep_time = {item: count for item ,count in counts.items() if count > 1}
print("Repeated items: ", rep_time)

target=int(input("Enter target value: "))

print(f"{target} appears { counts[target]} times")