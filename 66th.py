"""WAP to store multiple student details as list of tuple and display in each tuple name roll and marks, display who scored above 75"""
students = [
    ("Mohammad" , 101 , 85),
    ("Abdullah" , 102 , 95),
    ("Rasgulla" , 103 , 90),
    ("Habibulla" , 104 , 89)
]

print("Students who scored above 75: ")

for student in students:
    name , roll , marks = student

    if marks > 75:
        print(name , roll , marks)

