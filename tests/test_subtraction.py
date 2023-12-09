import unittest as ut

# test하고 싶은 메소드 import
#---------------------------Factorial test-----------------------------
from operators.subtraction import subtraction
from calculator import calculator

# test class
#----------------------------------------------------------------------
class TestSubtraction(ut.TestCase):
    def test_subtraction_one(self):
        self.assertEqual(subtraction(1, 2), -1)
        self.assertEqual(calculator([1, "-", 2]), -1)
        self.assertEqual(calculator(["1", "-", "2"]), -1)

    def test_subtraction_zero(self):
        self.assertEqual(subtraction(0, 0), 0)
        self.assertEqual(calculator([0, "-", 0]), 0)
        self.assertEqual(calculator(["0", "-", "0"]), 0)

    def test_subtraction_large_numbers(self):
        self.assertEqual(subtraction(1000000, 2000000), -1000000)
        self.assertEqual(calculator([1000000, "-", 2000000]), -1000000)
        self.assertEqual(calculator(["1000000", "-", "2000000"]), -1000000)

    def test_subtraction_positive_negative(self):
        self.assertEqual(subtraction(200000- 1000), 199000)
        self.assertEqual(calculator([200000, "-", 1000]), 199000)
        self.assertEqual(calculator(["200000", "-", "1000"]), 199000)

if __name__ == '__main__':
    ut.main()