import sys

from calculator import calculator
from error import validator
from easteregg import easteregg

stack = []
user_input = ""
state = 0

# = 가 입력되기 전까지 계속해서 입력을 받는다.
while user_input != "=":
    user_input = input("").strip()
    
    easter = easteregg(user_input)
    if easter != 0:
        print("[EVENT]", easter)
        
    state, user_input = validator(state, stack, user_input)
    
    if state == 3:
        print("[SYSTEM]", user_input)
        sys.exit()
    
    stack.append(user_input)
    
# = 입력 후...여기서 연산 결과 처리

print(calculator(stack))
