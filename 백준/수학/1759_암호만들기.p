'''
<문제분석>
L = 서로다른소문자 알파벳의 개수
C = 사용했을 법한 문자 종류의 개수
암호는 최소 한 개의 모음 + 최소 두 개의 자음으로 구성

1) 사전순으로 나열한다고 했으니 입력받은 문자죵류의 알파벳들을 정렬한다
2) 정렬되었다면, 암호를 만들 수 있는 알파벳 경우의 수를 정하기 위해 재귀로 돌림
3) 암호를 조합한다 자음과 모음의 개수를 확인
4) 암호 조합한 후에 남아있는 암호목록을 재귀로 돌림
5) 조건에 맞는 암호 추가

* 모음이 존재하는지 확인하기 위해 o(1) 이걸리는 해시맵을 통해서 in 을 사용하였다.
'''

L, C = map(int, input().split())
alpha = input().split()
alpha.sort()

#aeiou = ['a', 'e', 'i', 'o', 'u']
aeiou = {
    'a' : {},
    'e' : {},
    'i' : {},
    'o' : {},
    'u' : {}
}

result = []

def code(input: list, passw: str, length: int, index: int, jaum: int, moum: int):
    
    if not input:
        return
    print(input, passw, length, index, jaum, moum)
    if len(input) > L - length : # 2) 조합 가능한 알파벳의 경우의 수 재귀
        print('1')
        code(input[index+1:], passw, length, 0, jaum, moum)

    # 3) 알파벳 조합 (자음, 모음 카운트)
    passw = passw + input[index]; length = len(passw) 
    if(input[index] in aeiou): moum += 1
    else: jaum += 1

    # 4) 조합 후 남은 알파벳 목록 추출
    if len(input) >= L - length and length < L:
        print('2')
        code(input[index+1:], passw, length, 0, jaum, moum)
    
    # 5) 알파벳 4글자 만든 후 모음 1개이상, 자음 2개이상 조건 만족시 가능한 암호결과에 추가
    if(len(passw) == L and moum >=1 and jaum >= 2):
            #print(passw)
            result.append(passw)
            return

    #print(input, passw, length, index, jaum, moum)

    
code(alpha, '', 0, 0, 0 , 0)
result.sort()

for r in result:
    print(r)






'''
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은,
702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. 
C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 
주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력)
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

ex)
4 6
a t c i s w

acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''