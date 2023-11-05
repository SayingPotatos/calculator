from calculator import calculator

stack = []
user_input = ""

# = 가 입력되기 전까지 계속해서 입력을 받는다.
while user_input != "=":
    user_input = input("")
    stack.append(user_input)

# = 입력 후...여기서 연산 결과 처리

calculator(stack)