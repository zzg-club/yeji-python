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
