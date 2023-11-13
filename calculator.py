# TODO: 입력 스택을 받아 알맞은 연산자를 처리하고 에러와 이스터에그 분기를 처리한다.

# file 경로 설정
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
operator_dir = os.path.join(script_dir, 'operator')
sys.path.append(operator_dir)

# 연산자 import
from addition import addition
from subtraction import subtraction
from multiplication import multiplication

# 에러, 이스터에그 import 
from error import validator
from error import noiseFilter
from easteregg import easteregg

def calculator(args):
    noiseFilter(args)
    
    # 수식
    print(args)
    easteregg(args)
    
    # 여기서 사칙연산처리
    if (validator(args)):
        # 연산
    else:
        print("ERROR")

    return 0