"""WAp to store one student data as a tuple : name , roll no , and marks display the grade based on marks"""

name = input("Enter name: ")
roll = int(input("Enter roll: "))
marks = float(input("Enter marks: "))

student = (name,roll,marks)
print(student)

if(marks>=90):
    print("Distinction")
elif(marks>=75):
    print("Good")
elif(marks>=50):
    print("Average")
elif(marks>=33):
    print("Border Pass")
elif(marks>=0):
    print("Fail")

