"""
Ragvir Hothi
Python data and functions
"""
print("--------- example 1: dictionary------------")
car ={
    "brand": "Tesla",
    "model": "S",
    "year": 2023
}

print(f"Best car 2022 = {car['brand']}, model = {car['model']}")

print("\n--------example 2: loop through each key in a dictionary---------")
for k in car:
    print(f"{k} has a value of {car[k]}")

print("\n-------example 3: among of key-pair in a dictionary-------")
print(f"dictionary has {len(car)}")

print("\n-------example 4: remove a key-value pair from a dictionary----")
car.pop("year")
print(f"dictionary after removing the 'year' key")
for k in car:
    print(f"{k}, {car[k]}")

print("----------example 5: get value of a key-------")
look_key = "last_visit"
print(f"The value of key {look_key} is {car.get(look_key)}")

print("\n-------example 6: store data in a dictionary------")
phrase = "to be or not to be"
phrase = phrase.split()
print(f"phrase after split method {phrase}")
word_count_dict = {} #empty dictionary

for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)

print("\n---------EXCERCISE---------")
# given follow list; find users using gmail, hotmail, and yahoo
#loop to go through each word
#save the count of emails in a dictionary
email_lister = {"gmail": 0, "hotmail": 0, "yahoo": 0}
user = '''
    'peter' = 'ppan@gmail.com',
    'diana' = 'd@hotmail.com',
    'Kent' = 'ckent@yahoo.com',
    'Bruce' = 'bwayne@hotmail.com',
    'tony' = 'tstark@gmail.com',
    'shrek' = 'shrek@gmail.com'
'''

user_lines = user.strip().split('\n')

for line in user_lines:
    email = line.split('=')[1].strip().strip("'").strip(',')
    
    if '@gmail' in email:
        email_lister["gmail"] += 1
    elif '@hotmail' in email:
        email_lister["hotmail"] += 1
    elif '@yahoo' in email:
        email_lister["yahoo"] += 1

print(email_lister)