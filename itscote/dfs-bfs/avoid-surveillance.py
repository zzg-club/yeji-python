# 기출-20 감시 피하기
# https://www.acmicpc.net/problem/18428

from itertools import combinations
import copy

n = int(input())
map_info = [list(map(str, input().split())) for _ in range(n)]

tch = []
std = []
blank = []

for i in range(n):
    for j in range(n):
        if map_info[i][j] == 'S':
            std.append([i, j])
        elif map_info[i][j] == 'T':
            tch.append([i, j])
        else:
            blank.append([i, j])

ud = [-1, 0, 1, 0]
lr = [0, 1, 0, -1]

# 감시 피하기 성공 = True, 실패 = False
def check(x, y, temp_map):
    for i in range(4): # 상 하 좌 우 살핌
        nx, ny = x, y  # 교사 위치 기준 시작
        while 0 <= nx < n and 0 <= ny < n: # map 내부에 좌표가 존재하면 계속 루프 돌면서 탐색
            nx += ud[i]
            ny += lr[i]
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if temp_map[nx][ny] == 'O':
                break
            if temp_map[nx][ny] == 'S':
                return False
    return True

result = "NO"

for obs in combinations(blank, 3):
    temp_map = copy.deepcopy(map_info)

    # 장애물 세우기
    for x, y in obs:
        temp_map[x][y] = 'O'

    # 각 선생님 위치당 check -> 한 명이라도 False면 
    temp_result = True
    for teacher in tch:
        if not check(teacher[0], teacher[1], temp_map):
            temp_result = False
            break

    if temp_result:
        result = "YES"

print(result)