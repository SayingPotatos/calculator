import unittest as ut
from operators.subtraction import subtraction
from calculator import calculator

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
        self.assertEqual(subtraction(200000, 1000), 199000)
        self.assertEqual(calculator([200000, "-", 1000]), 199000)
        self.assertEqual(calculator(["200000", "-", "1000"]), 199000)

def suite():
    test_suite = ut.TestSuite()
    test_suite.addTest(TestSubtraction('test_subtraction_one'))
    test_suite.addTest(TestSubtraction('test_subtraction_zero'))
    test_suite.addTest(TestSubtraction('test_subtraction_large_numbers'))
    test_suite.addTest(TestSubtraction('test_subtraction_positive_negative'))
    return test_suite

if __name__ == '__main__':
    runner = ut.TextTestRunner()
    runner.run(suite())
