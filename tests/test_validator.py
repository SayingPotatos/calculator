import unittest as ut

# test하고 싶은 메소드 import
#---------------------------validator test-----------------------------
from error import validator

class TestValidator_add(ut.TestCase):
    # 정상 덧셈에 대한 test
    def test_1(self):
        test_input = ["1", "+", "1", "="]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 1, 4]
        test_output2 = [1, "+", 1, "="]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
    
    # 비정상 덧셈 입력에 대한 test(숫자 연속 입력)
    def test_2(self):
        test_input = ["1", "+", "3", "3"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 1, 3]
        test_output2 = [1, "+", 3, "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
    # 비정상 덧셈 입력에 대한 test(연산자 연속 입력)
    def test_3(self):
        test_input = ["1", "+", "+"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 3]
        test_output2 = [1, "+", "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
class TestValidator_subs(ut.TestCase):
    # 정상 뺄셈에 대한 test
    def test_4(self):
        test_input = ["1", "-", "1", "="]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 1, 4]
        test_output2 = [1, "-", 1, "="]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
    
    # 비정상 뺄셈 입력에 대한 test(숫자 연속 입력)
    def test_5(self):
        test_input = ["1", "-", "3", "3"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 1, 3]
        test_output2 = [1, "-", 3, "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
    # 비정상 뺄셈 입력에 대한 test(연산자 연속 입력)
    def test_6(self):
        test_input = ["1", "-", "-"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 3]
        test_output2 = [1, "-", "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
class TestValidator_multi(ut.TestCase):
    # 정상 곱셈에 대한 test
    def test_7(self):
        test_input = ["1", "x", "1", "="]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 1, 4]
        test_output2 = [1, "x", 1, "="]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
    
    # 비정상 곱셈 입력에 대한 test(숫자 연속 입력)
    def test_8(self):
        test_input = ["1", "x", "3", "3"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 1, 3]
        test_output2 = [1, "x", 3, "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
    # 비정상 곱셈 입력에 대한 test(연산자 연속 입력)
    def test_9(self):
        test_input = ["1", "x", "x"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 2, 3]
        test_output2 = [1, "x", "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
    # 비정상 곱셈 입력에 대한 test(연산자 연속 입력)
    def test_10(self):
        test_input = ["1", "*"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 3]
        test_output2 = [1, "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
class TestValidator_factorial(ut.TestCase):
    # 정상 팩토리얼 입력에 대한 test
    def test_11(self):
        test_input = ["1", "!", "="]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 1, 4]
        test_output2 = [1, "!", "="]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
    
    # 숫자 연속 입력에 대한 test, 비정상 입력
    def test_12(self):
        test_input = ["1", "1"]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 3]
        test_output2 = [1, "Input Error"]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1
            
    # 정상 팩토리얼 입력에 대한 test(연산자 연속 입력(숫자 계산에서 팩토리얼은 연속 입력이 가능함))
    def test_13(self):
        test_input = ["1", "!", "!", "="]
        input_num = 0 #input 횟수
        state = 0
        test_output1 = [1, 1, 1, 4]
        test_output2 = [1, "!", "!", "="]
        stack = []
        for t in test_input:
            state, converted_user_input = validator(state, t)
            self.assertEqual(test_output1[input_num], state)
            self.assertEqual(test_output2[input_num], converted_user_input)
            stack.append(converted_user_input)
            input_num += 1

# "="을 제외한 모든 연산자는 비정상 입력  
class TestValidator_startWithOperator(ut.TestCase):
    def test_14(self):
        test_input = "!"
        test_output1 = 3
        test_output2 = "Input Error"
        state = 0
        stack = [test_input]
        state, converted_user_input = validator(state, test_input)
        self.assertEqual(test_output1, state)
        self.assertEqual(test_output2, converted_user_input)
    
    def test_15(self):
        test_input = "x"
        test_output1 = 3
        test_output2 = "Input Error"
        state = 0
        stack = [test_input]
        state, converted_user_input = validator(state, test_input)
        self.assertEqual(test_output1, state)
        self.assertEqual(test_output2, converted_user_input)
        
    def test_16(self):
        test_input = "+"
        test_output1 = 3
        test_output2 = "Input Error"
        state = 0
        stack = [test_input]
        state, converted_user_input = validator(state, test_input)
        self.assertEqual(test_output1, state)
        self.assertEqual(test_output2, converted_user_input)
        
    def test_17(self):
        test_input = "-"
        test_output1 = 3
        test_output2 = "Input Error"
        state = 0
        stack = [test_input]
        state, converted_user_input = validator(state, test_input)
        self.assertEqual(test_output1, state)
        self.assertEqual(test_output2, converted_user_input)
    
    # "="은 정상 종료
    def test_18(self):
        test_input = "="
        test_output1 = 4
        test_output2 = "="
        state = 0
        stack = [test_input]
        state, converted_user_input = validator(state, test_input)
        self.assertEqual(test_output1, state)
        self.assertEqual(test_output2, converted_user_input)
#----------------------------------------------------------------------

if __name__ == '__main__':
    validator_add_suite = ut.TestSuite()
    validator_add_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestValidator_add))
    
    validator_subs_suite = ut.TestSuite()
    validator_subs_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestValidator_subs))

    validator_multi_suite = ut.TestSuite()
    validator_multi_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestValidator_multi))
    
    validator_factorial_suite = ut.TestSuite()
    validator_factorial_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestValidator_factorial))
    
    validator_startWithOperator_suite = ut.TestSuite()
    validator_startWithOperator_suite.addTests(ut.TestLoader().loadTestsFromTestCase(TestValidator_startWithOperator))
    
    # validator 관련 suite들을 하나로 묶음
    all_validator_suites = ut.TestSuite([validator_add_suite, validator_subs_suite, validator_multi_suite, validator_factorial_suite, validator_startWithOperator_suite])
    
    # 팩토리얼 suites에 대한 test실행
    ut.TextTestRunner().run(all_validator_suites)
