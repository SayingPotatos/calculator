import unittest as ut
from operators.multiplication import multiplication
from calculator import calculator

class TestMultiplication(ut.TestCase):
    def test_multiplication_one(self):
        self.assertEqual(multiplication(1, 2), 2)
        self.assertEqual(calculator([1, "x", 2]), 2)
        self.assertEqual(calculator([1, "*", 2]), 2)
        self.assertEqual(calculator(["1", "x", "2"]), 2)

    def test_multiplication_zero(self):
        self.assertEqual(multiplication(0, 0), 0)
        self.assertEqual(calculator([0, "x", 0]), 0)
        self.assertEqual(calculator([0, "*", 0]), 0)
        self.assertEqual(calculator(["0", "x", "0"]), 0)

    def test_multiplication_large_numbers(self):
        self.assertEqual(multiplication(1000000, 2000000), 2000000000000)
        self.assertEqual(calculator([1000000, "x", 2000000]), 2000000000000)
        self.assertEqual(calculator([1000000, "*", 2000000]), 2000000000000)
        self.assertEqual(calculator(["1000000", "x", "2000000"]), 2000000000000)

def suite():
    test_suite = ut.TestSuite()
    test_suite.addTest(TestMultiplication('test_multiplication_one'))
    test_suite.addTest(TestMultiplication('test_multiplication_zero'))
    test_suite.addTest(TestMultiplication('test_multiplication_large_numbers'))
    return test_suite

if __name__ == '__main__':
    runner = ut.TextTestRunner()
    runner.run(suite())
