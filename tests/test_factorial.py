import unittest as ut

# test하고 싶은 메소드 import
#---------------------------Factorial test-----------------------------
from operators.factorial import factorial

# test class
# 음수 입력시 에러 코드 
class TestFactorial_InputLess0(ut.TestCase):
    def test_1(self): 
        self.assertEqual(factorial(-1), "Out Of Range") 
        
    def test_2(self):
        test_input = -10
        test_output = "Out Of Range"
        self.assertEqual(test_output, factorial(test_input))

# 0 입력시 동작
class TestFactorial_Input0(ut.TestCase):
    def test_3(self):
        test_input = 0
        test_output = 1
        self.assertEqual(test_output, factorial(test_input))

class TestFactorial_InputNormal(ut.TestCase):

    def test_4(self):
        test_input = 3
        test_output = 6
        self.assertEqual(test_output, factorial(test_input))
        
        
if __name__ == '__main__':
    factorial_inputLess0_suite = ut.TestSuite()
    factorial_inputLess0_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestFactorial_InputLess0))

    factorial_input0_suite = ut.TestSuite()
    factorial_input0_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestFactorial_Input0))

    factorial_inputNormal_suite = ut.TestSuite()
    factorial_inputNormal_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestFactorial_InputNormal))

    # 팩토리얼 관련 suite들을 하나로 묶음
    all_factorial_suites = ut.TestSuite([factorial_inputLess0_suite, factorial_input0_suite, factorial_inputNormal_suite])

    # 팩토리얼 suites에 대한 test실행
    ut.TextTestRunner().run(all_factorial_suites)
