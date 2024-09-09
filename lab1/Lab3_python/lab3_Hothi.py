"""
Ragvir Hothi
Lab 3, Python review
"""
print("----------Example 1: control flow--------------")
labs = int(input("Enter labs' grades :"))
exams = int(input("Enter exams' grade: "))
finalgrade = 0
gpa = ''

if(0<=labs<=100 and 0<=exams<=100):
    finalgrade = (labs + exams) / 2
    if(100>=finalgrade>=90):
        gpa = 'A'
    elif(90>finalgrade>=80):
        gpa = 'B'
    elif(80>finalgrade>=70):
        gpa = 'C'
    elif(70>finalgrade>=60):
        gpa = 'D'
    elif(60>finalgrade>=0):
        gpa = 'F'
    else:
        gpa = 'UNDEFINED'
else:
    if not(0<=labs<=100):
        print(f"Grade for lab {labs} is invalid")
    elif not(0<=exams<=100):
        print(f"Grade for exams {exams} is invalid")
    else:
        print(f"Grade for labs = {labs} and exams = {exams} are invalid")
    gpa = 'UNDEFINED'
print(f"Your final grade for the class is {finalgrade} = {gpa}")