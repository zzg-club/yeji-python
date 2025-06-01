# 기출-21 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]

ud = [1, 0, -1, 0]
lr = [0, 1, 0 , -1]
opposite = [1, 0, 3, 2]  # 반대 방향

# 3차원 배열에다가 
def update_border(x,y,border):
    flag = False
    for i in range(4):
        nx = x + ud[i]
        ny = y + lr[i]
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if l <= abs(map_info[x][y] - map_info[nx][ny]) <= r:
            border[x][y][i] = True
            border[nx][ny][opposite[i]] = True
            flag = True
    return flag


def bfs(x, y, visited, border):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)] # 연합 국가 좌표 리스트
    total = map_info[x][y] # 연합의 총 인구수

    while q:
        i, j = q.popleft()
        for d in range(4):
            if not border[i][j][d]: # 국경이 닫혀있으면 무시
                continue

            # 국경이 열려 있는 경우
            ni = i + ud[d]
            nj = j + lr[d]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                union.append((ni, nj)) # 연합에 추가
                total += map_info[ni][nj] # 연합의 총 인구수에 누적 추가
    return union, total

count = 0
while True:
    # 국경 초기화 - 모두 닫힌 상태
    border = [[[False] * 4 for _ in range(n)] for _ in range(n)]

    # 국경 열림/닫힘 정보 저장
    for i in range(n):
        for j in range(n):
            update_border(i, j, border)

    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total = bfs(i, j, visited, border)
                if len(union) > 1:
                    avg = total // len(union) # 연합 국가들의 인구수 계산
                    for ux, uy in union:
                        map_info[ux][uy] = avg
                    moved = True

    # 국경만 열리고 이동이 일어나지 않은 경우에는.. count하지 않음
    if not moved:
        break

    count += 1

print(count)
        