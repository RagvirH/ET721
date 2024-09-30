"""
example 3: verify if the email, full name, and salary field are correct
Ragvir Hothi
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    #set up of templates
    def setUp(self):
        #create an instance of the class Employee
        self.emp1 = Employee("Bruce","Wayne", 1000000)

    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee,"BruceWayne@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Wayne Bruce")

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.salary, 1050000)
if __name__ == "__main__":
    unittest.main()