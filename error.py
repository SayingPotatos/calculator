# TODO: 정상적인 수식인지 확인 및 에러 시 동작
import copy

# 0 반환시 ERROR
# 1 반환시 계산 수행
def validator(args):    
    # 원본 변수에 영향을 주지 않기 위해 깊은 복사를 수행    
    _args = copy.deepcopy(args)
    
    # 정해진 연산자
    ops = ['+', '-', 'x', '=']
    
    for i in range(len(_args)):
        if (i % 2 == 0):
            try:
                _args[i] = int(_args[i])
            except ValueError:
                # 정수가 입력되어야 하는데 정수 형태의 입력이 아님
                return 0
        else:
            # 정해진 연산자 이외의 입력이 들어옴
            if _args[i] not in ops:
                return 0
    
    return 1

def noiseFilter(args):
    # 원소 내부의 공백 제거
        args[i] = args[i].strip();