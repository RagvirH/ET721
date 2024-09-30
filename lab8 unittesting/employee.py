"""
example 3: verify if the email, full name, and salary field are correct
Ragvir Hothi
"""

class Employee:
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary

    #property decorator indicates that the method will behave like an attribute
    @property
    def emailemployee(self):
        return f"{self.first}{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary = int(self.salary*self.raise_amt)