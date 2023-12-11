# 연산자 import
from operators.factorial import factorial

# TODO: 정상적인 입력인지 확인 및 에러 시 동작
#- 비정상 입력 예시(더 있을 수 있음)
#    ["0","+","+"]
#    ["0","-","1","1"]
#    ["+", "="]
def isInt(n):
    _s = n
    try:
        _s = int(_s)
    except ValueError:
        return False
    return True

# ERROR 발생 시 str 객체 반환
def validator(state, u):    
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
        elif u == "!":
            state = 1
        else:
            state = 3
    elif state == 2:
        if isInt(u):
            state = 1
        else:
            state = 3 
        
    if state == 3:
        u = err_out

    # 스택 내의 숫자형 문자열을 정수형으로 변환해주는 코드
    if isInt(u):
        u = int(u)

    return state, u
