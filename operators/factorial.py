def factorial(num):
    _num = num
    ret = 1
    if _num == 0:
        return 1
    elif _num < 0:
        return "Out Of Range"
    else:
        while _num != 1:
            ret = ret * _num
            _num -= 1
            
    return ret          