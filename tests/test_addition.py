import unittest as ut
from operators.addition import addition
from calculator import calculator

class TestAddition(ut.TestCase):
    def test_addition_one(self):
        self.assertEqual(addition(1, 2), 3)
        self.assertEqual(calculator([1, "+", 2]), 3)
        self.assertEqual(calculator(["1", "+", "2"]), 3)

    def test_addition_zero(self):
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(calculator([0, "+", 0]), 0)
        self.assertEqual(calculator(["0", "+", "0"]), 0)

    def test_addition_large_numbers(self):
        self.assertEqual(addition(1000000, 2000000), 3000000)
        self.assertEqual(calculator([1000000, "+", 2000000]), 3000000)
        self.assertEqual(calculator(["1000000", "+", "2000000"]), 3000000)

if __name__ == '__main__':
    ut.main()