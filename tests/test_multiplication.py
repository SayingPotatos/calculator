import unittest as ut

# test하고 싶은 메소드 import
#---------------------------Factorial test-----------------------------
from operators.multiplication import multiplication
from calculator import calculator

# test class
#----------------------------------------------------------------------
class TestMultiplication(ut.TestCase):
    def test_multiplication_one(self):
        self.assertEqual(multiplication(1, 2), 2)
        self.assertEqual(calculator([1, "*", 2]), 2)
        self.assertEqual(calculator(["1", "*", "2"]), 2)

    def test_multiplication_zero(self):
        self.assertEqual(multiplication(0, 0), 0)
        self.assertEqual(calculator([0, "*", 0]), 0)
        self.assertEqual(calculator(["0", "*", "0"]), 0)

    def test_multiplication_large_numbers(self):
        self.assertEqual(multiplication(1000000, 2000000), 2000000000000)
        self.assertEqual(calculator([1000000, "*", 2000000]), 2000000000000)
        self.assertEqual(calculator(["1000000", "*", "2000000"]), 2000000000000)

if __name__ == '__main__':
    ut.main()