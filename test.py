import unittest as ut

# test하고 싶은 메소드 import
#---------------------------Factorial test-----------------------------
from operators.factorial import factorial

class TestFactorial_InputLess0(ut.TestCase):
    def test_1(self):
        test_input = -1
        test_output = "Out Of Range"
        self.assertEqual(test_output, factorial(test_input))
        
    def test_2(self):
        test_input = -10
        test_output = "Out Of Range"
        self.assertEqual(test_output, factorial(test_input))

class TestFactorial_Input0(ut.TestCase):
    def test_3(self):
        test_input = 0
        test_output = 1
        self.assertEqual(test_output, factorial(test_input))
        
class TestFactorial_InputGreater0(ut.TestCase):
    def test_4(self):
        test_input = 5
        test_output = 120
        self.assertEqual(test_output, factorial(test_input))
        
    def test_5(self):
        test_input = 10
        test_output = 3628800
        self.assertEqual(test_output, factorial(test_input))
#----------------------------------------------------------------------

if __name__ == '__main__':
    factorial_inputLess0 = ut.TestSuite()
    factorial_inputLess0.addTests(ut.TestLoader().loadTestsFromTestCase(TestFactorial_InputLess0))
    
    factorial_input0_suite = ut.TestSuite()
    factorial_input0_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestFactorial_Input0))
    
    factorial_inputGreater0_suite = ut.TestSuite()
    factorial_inputGreater0_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestFactorial_InputGreater0))
    
    # 팩토리얼 관련 suite들을 하나로 묶음
    all_factorial_suites = ut.TestSuite([factorial_inputLess0, factorial_input0_suite, factorial_inputGreater0_suite])
    
    # 팩토리얼 suites에 대한 test실행
    ut.TextTestRunner().run(all_factorial_suites)