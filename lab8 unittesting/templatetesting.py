import unittest

def AddTwoNumbers(a, b):
    return a+b


# create a unit test to check if function 'AddTwoNumbers' is working properly
class TestAddFunction(unittest.TestCase):
    def test_AddTwoNumbers(self):
        self.assertEqual(AddTwoNumbers(3, 5 ), 8)

if __name__ == '__main__':
    unittest.main()