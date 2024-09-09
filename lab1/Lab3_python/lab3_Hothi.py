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

print("---------Example 2: Loops, guess number------------")
SECRET = 8
userguess = int(input("Guess a number between 1 and 10: "))
while not(SECRET == userguess):
    userguess = int(input("wrong guess. Guess again: "))

print(f"Congrats! {userguess} is the right number!")

print("-----------Example 3: Loops, break statement-----------")
balance = 1000
withdraw = 0
deposit = 0

while True:
    userinput = input("Do you want to withdraw, w or deposit, d? ")
    if userinput == 'w' or userinput == 'W':
        w_amount = int(input('How much would you like to withdraw?'))
        if w_amount>balance:
            print(f"Insufficient funds! You cannot withdraw more than {balance}")
        else:
            balance -=w_amount
            print(f"Your new balance is {balance}")
    elif userinput =='d' or userinput =='D':
        d_amount = int(input('How much do you want to deposit?'))
        balance += d_amount
        print(f"Your new balance is {balance}")
    else:
        print("Invalid selection!")

    choice = input("Would you like to do another transaction? (y,n)")
    if not(choice=='y' or choice =='Y'):
        break
print("Thank you for banking with us!")