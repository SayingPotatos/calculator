# TODO: 특정 숫자가 입력되었는지 판별 후, 맞으면 이스터에그 표시
import copy

def easteregg(args):
    _args = copy.deepcopy(args)
    
    if _args == 1126611:
        return '사랑해'
    elif _args == 9090:
        return '가자'
    elif _args == 982:
        return '잘 가'
    elif _args == 827:
        return '파이팅'
    elif _args == 11010:
        return '흥'
    elif _args == 825:
        return '빨리 와'
    elif _args == 2222:
        return '투덜투덜'
    elif _args == 505:
        return 'SOS'
    elif _args == 230:
        return '이상 없음'
    elif _args == 100:
        return '돌아와'
    elif _args == 175:
        return '일찍 와'
    elif _args == 981:
        return '급한 일이 생겼어'
    elif _args == 337:
        return '힘내'
    elif _args == 1004:
        return '천사'
    elif _args == 9431:
        return '구사일생'
    elif _args == 1414:
        return '밥먹자'
    elif _args == 952:
        return '좋은 아침'
    elif _args == 1008:
        return '고민 중'
    elif _args == 1225:
        return 'MerryChristmas!'
    else:
        return ' '


