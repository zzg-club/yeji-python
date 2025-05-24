# 기출-16 연구소
# https://www.acmicpc.net/problem/14502

n, m = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]  # 입력 오류 수정

ud = [-1, 0, 1, 0]
lr = [0, 1, 0, -1]

def dfs(x, y, count):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return

    for i in range(4):  # 4방향만 탐색
        nx = x + ud[i]
        ny = y + lr[i]
        if 0 <= nx < n and 0 <= ny < m and map_info[nx][ny] == 0:
            if count > 0:
                map_info[nx][ny] = 1  # 벽 세우기
            else:
                dfs(nx, ny, count + 1)

def virus(x, y):
    for i in range(4):
        nx = x + ud[i]
        ny = y + lr[i]
        if 0 <= nx < n and 0 <= ny < m and map_info[nx][ny] == 0:
            map_info[nx][ny] = 2
            virus(nx, ny)

# 벽 세우기 - dfs 사용 시도
for i in range(n):
    for j in range(m):
        if map_info[i][j] == 0:
            dfs(i, j, 0)

# 바이러스 퍼뜨리기
for i in range(n):
    for j in range(m):
        if map_info[i][j] == 2:
            virus(i, j)

# 안전 영역 계산
result = 0
for i in range(n):
    for j in range(m):
        if map_info[i][j] == 0:
            result += 1

print(result)


# --------------------------------

from itertools import combinations
import copy

n, m = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]

ud = [-1, 0, 1, 0]
lr = [0, 1, 0, -1]

def virus(x, y, temp_map):
    for i in range(4):
        nx = x + ud[i]
        ny = y + lr[i]
        if 0 <= nx < n and 0 <= ny < m and temp_map[nx][ny] == 0:
            temp_map[nx][ny] = 2
            virus(nx, ny, temp_map)

def get_safe_area(temp_map):
    result = 0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                result += 1
    return result

# 0인 공간 위치 수집
empty_spaces = [(i, j) for i in range(n) for j in range(m) if map_info[i][j] == 0]

max_safe = 0

# 벽 3개 세우는 조합들
for walls in combinations(empty_spaces, 3):
    temp_map = copy.deepcopy(map_info)

    # 벽 세우기
    for x, y in walls:
        temp_map[x][y] = 1

    # 바이러스 퍼뜨리기
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                virus(i, j, temp_map)

    # 안전 영역 계산
    safe = get_safe_area(temp_map)
    max_safe = max(max_safe, safe)

print(max_safe)
