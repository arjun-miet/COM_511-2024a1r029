""" WAP to input mrks of 10 students in a list , display highest mrks , lowest , average and no of students who passed"""

ls = list(map(int,input("Enter Marks: ").split()))

print("Max marks: ", max(ls))
print("Min marks: ", min(ls))
print("Avg marks: ", sum(ls)/len(ls))
passed=0
for x in ls:
    if x>40:
        passed+=1

print("Passed: ",passed) 
