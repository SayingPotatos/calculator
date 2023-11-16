# TODO: 특정 숫자가 입력되었는지 판별 후, 맞으면 이스터에그 표시

def easteregg(args):
    dictionary = {
            '1126611': '사랑해',
            '9090': '가자',
            '982': '잘 가',
            '827': '파이팅',
            '11010': '흥',
            '825': '빨리 와',
            '2222': '투덜투덜',
            '505': 'SOS',
            '230': '이상 없음',
            '100': '돌아와',
            '175': '일찍 와',
            '981': '급한 일이 생겼어',
            '337': '힘내',
            '1004': '천사',
            '9431': '구사일생',
            '1414': '밥먹자',
            '952': '좋은 아침',
            '1008': '고민 중',
            '1225': 'Merry Christmas!',
        }
        
    return dictionary.get(args, 0)

    # result = dictionary.get(args, None)

    # if result is not None:
    #     print(result)
    
    # return result

