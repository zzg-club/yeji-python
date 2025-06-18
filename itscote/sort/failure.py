# 기출 25) 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    clear = [0] * N
    noclear = [0] * N
    failure = []

    for stage in stages:
        if 1 <= stage <= N:
            noclear[stage - 1] += 1
        
        if stage > N:
            for i in range(N):
                clear[i] += 1
        else:
            for i in range(stage):
                clear[i] += 1

    for i in range(N):
        if clear[i] == 0:
            failure.append([i + 1, 0])
        else:
            failure.append([i + 1, noclear[i] / clear[i]])

    failure.sort(key=lambda x: -x[1])

    for i in range(N):
        answer.append(failure[i][0])

    return answer
