"""Create a text file named MyFile.txt in Python and ask the user to write three separate lines using three input statements."""
f = open("MyFile.txt", "w")

line1 = input("Enter first line: ")
line2 = input("Enter second line: ")
line3 = input("Enter third line: ")

f.write(line1 + "\n")
f.write(line2 + "\n")
f.write(line3 + "\n")

f.close()

print("Data written successfully!")
