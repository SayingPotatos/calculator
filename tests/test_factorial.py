import unittest as ut

# test하고 싶은 메소드 import
#---------------------------Factorial test-----------------------------
from operators.factorial import factorial

# test class
#----------------------------------------------------------------------
class TestFactorial(ut.TestCase):
    def test_1(self): 
        self.assertEqual(factorial(-1),"[ERROR] Out Of Range") #음수 입력시 에러 코드 
        
if __name__ == '__main__':
    # 러닝 코드용
    ut.main(exit=False)
