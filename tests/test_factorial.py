import unittest as ut

# test하고 싶은 메소드 import
#---------------------------Factorial test-----------------------------
from operators.factorial import factorial

# test class
# 음수 입력시 에러 코드 
class TestFactorial_InputLess0(ut.TestCase):
    def test_1(self): 
        self.assertEqual(factorial(-1),"[ERROR] Out Of Range") 

# 0 입력시 동작
class TestFactorial_Input0(ut.TestCase):
    def test_3(self):
        test_input = 0
        test_output = 1
        self.assertEqual(test_output, factorial(test_input))
#----------------------------------------------------------------------

        
if __name__ == '__main__':
    # 러닝 코드용
    ut.main(exit=False)