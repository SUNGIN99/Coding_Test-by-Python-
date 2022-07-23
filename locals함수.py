import pprint

#pprint.pprint(locals())

def funct1():
    # 클래스, 함수 내 모든 지역변수 조회
    
    i = 10;
    pprint.pprint(locals())

    return i;

print(funct1())