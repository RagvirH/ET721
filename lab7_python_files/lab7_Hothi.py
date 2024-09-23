"""
Ragvir Hothi
Sept 23, Python files
"""

print("----------Example 1: Python files------------")
#pipe the user.txt file

fileusers = open("users.txt", "r")
for eachline in fileusers:
    print(eachline)
print("\n----------Example 2: Python limit to read files --------")
#read the first ten characters
print(fileusers.read(10))

#alternative: print(fileusers.read())
"""
use loop to go through each line of the file
for eachline in fileusers:
    print(eachline)

"""
#close file
fileusers.close()

print("\n------Example 3: Python read files with 'with' and 'readlines'-----------")
with open("users.txt", "r") as fileusers:
    eachline = fileusers.readlines()
    print(eachline[2])

print("\n---------Example 4: Python read files with'spilt()------------")
with open("users.txt", "r") as fileusers:
    eachline = fileusers.readlines()
    for line in eachline:
        word = line.split()
        print(word[2])

print("----------Example 5: Python read file and check for a specific item------------")
#loop to the 'users'txt' file and check how many users are named 'Bruce'

def finduser(textfile, username):
    with open(textfile, "r") as fileusers:
        usercounter = 0
        for line in fileusers:
            words = line.split()
            if username.lower() in [word.lower() for word in words]:
                usercounter += 1
    return usercounter

user = "Clark"
usercount = finduser("users.txt", user)
print(f"There are {usercount} occurrences of the name '{user}'.")
        
print("\n----------Example 6: Python write file---------")
def userreport(totalcount, username):
    with open("writeresult.txt", "w") as writeuserresult:
        writeuserresult.write(f"There is {totalcount} with the name {username}")

userreport(usercount, user)

print("\n-----------Example 7: Python appending data into a file--------")
def appenduser(newuser, city, age, userfilename):
    with open(userfilename, "a") as fileusers:
        fileusers.write(f"\n{newuser}, {city}, {age}")

appenduser("John", "New York", 30, "users.txt")
