import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_valid_withdrawal(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_invalid_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    def test_multiple_operations(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.account.deposit(100)
        self.account.withdraw(800)
        self.assertEqual(self.account.get_balance(), 600)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

if __name__ == '__main__':
    unittest.main()