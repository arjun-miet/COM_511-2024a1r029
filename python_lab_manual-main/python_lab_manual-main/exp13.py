''' Aim: Write a program that inputs a text file and prints all unique words in the file in alphabetical order.'''
import string

file = input("Enter file name: ")

f = open(file, "r")
text = f.read()
f.close()

words = text.split()

unique = set()

for word in words:
    word = word.strip(string.punctuation).lower()
    if word:
        unique.add(word)

print("Unique words in alphabetical order:")

for word in sorted(unique):
    print(word)
