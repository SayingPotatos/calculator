# 연산자 import
from operators.factorial import factorial

# TODO: 정상적인 수식인지 확인 및 에러 시 동작

# 0 반환시 ERROR
# 1 반환시 계산 수행
def validator(args):        
    # 정해진 연산자
    if state == 0:
        if isInt(u):
            state = 1
        elif u == "=":
            state = 4
        else:
            state = 3
    elif state == 1:
        go_2 = ["+", "-", "x"]
        if u in go_2:
            state = 2
        elif u == "=":
            state = 4
        elif u == "!":
            u = factorial(int(st.pop()))
            state = 1
            if isinstance(u, str):
                err_out = u
                state = 3
        else:
            state = 3
    elif state == 2:
        if isInt(u):
            state = 1
        else:
            state = 3 
        
    if state == 3:
        return state, u
    
    return state, u