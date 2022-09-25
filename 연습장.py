

import collections


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported_list = {} # 누가 누구를 신고했는지 -> 이메일 개수를 알 수 있음
    suspected_list = {} # 누가 누구에게 신고당했는지 -> 신고당한 횟수를 알수있음

    for index, name in enumerate(id_list):
        reported_list[name] = index
        suspected_list[name] = []


    for s in report:
        reporter, suspector = s.split()
        suspected_list[suspector].append(reporter)

            
    

    print('reported:  ', reported_list) # 신고자
    print('suspected: ', suspected_list) # 피의자
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
k = 2

#id_list = ["con", "ryan"]
#report = ["ryan con", "ryan con", "ryan con", "ryan con"]
#k = 3

print(solution(id_list, report, k))
#[2,1,1,0]


'''
    for s in report:
        reporter, suspector = s.split()
        reported_list[reporter][suspector] = 0
        suspected_list[suspector].append(reporter)


    for suspector, reporters in suspected_list.items():
        if len(suspected_list[suspector]) >= k:
            for reporter in reporters:
                reported_list[reporter][suspector] += 1

            
    

'''