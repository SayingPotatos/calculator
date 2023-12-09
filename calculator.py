# TODO: 입력 스택을 받아 알맞은 연산자를 처리하고 에러와 이스터에그 분기를 처리한다.

# file 경로 설정
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
operator_dir = os.path.join(script_dir, 'operator')
sys.path.append(operator_dir)

# 연산자 import
from operators.addition import addition
from operators.subtraction import subtraction
from operators.multiplication import multiplication

def multiple(args):
    while 'x' in args:
        index = args.index('x')
        result = multiplication(args[index-1], args[index+1])
        args[index-1:index+2] = [result]
    return args

def calculator(args):

    # print(args)

    # easteregg(args)

    args = multiple(args)
    
    # 여기서 사칙연산처리
    while '+' in args or '-' in args:
        if '+' in args:
            index = args.index('+')
            result = addition(args[index - 1], args[index + 1])
        elif '-' in args:
            index = args.index('-')
            result = subtraction(args[index - 1], args[index + 1])
        args[index - 1:index + 2] = [result]

    return args[0]
    # return 0