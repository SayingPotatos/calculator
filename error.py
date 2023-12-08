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
        return state, u
    
    return state, u

  # 0 반환시 ERROR
# 1 반환시 계산 수행
def validator(args):        
    # 정해진 연산자
    ops = ['+', '-', 'x', '=']
    
    for i in range(len(args)):
        if (i % 2 == 0):
            try:
                args[i] = int(args[i])
            except ValueError:
                # 정수가 입력되어야 하는데 정수 형태의 입력이 아님
                return 0
        else:
            # 정해진 연산자 이외의 입력이 들어옴
            if args[i] not in ops:
                return 0
    
    return 1

def noiseFilter(args):
    # 원소 내부의 공백 제거
    for i in range(len(args)):
        args[i] = args[i].strip();
