# 연산자 import
from operators.factorial import factorial

# TODO: 정상적인 수식인지 확인 및 에러 시 동작

def isInt(n):
    _s = n
    try:
        _s = int(_s)
    except ValueError:
        return False
    return True

# ERROR 발생 시 str 객체 반환
def validator(state, st, u):    
    err_out = "Input Error"    
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
        ## 추후 팩토리얼 추가시 활용
        # elif u == "!":
        #     state = 1
        else:
            state = 3
    elif state == 2:
        if isInt(u):
            state = 1
        else:
            state = 3 
        
    if state == 3:
        u = err_out
    
    if isInt(u):
        u = int(u)
    
    return state, u