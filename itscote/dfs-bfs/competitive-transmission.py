# 기출-17 경쟁적 전역
# https://www.acmicpc.net/problem/18405

n, k = map(int, input().split())
tube = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

ud = [1, 0 , -1, 0]
lr = [0, 1, 0, -1]

# 전염될 위치를 반환
def trans(x, y):
    result = []
    for i in range(4):
        nx = x + ud[i]
        ny = y + lr[i]
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if tube[nx][ny] == 0:
            result.append([tube[x][y], nx, ny]) # 상하좌우가 0이면 그 좌표와 값을 추가
    return result

for _ in range(s):
    virus_list = []
    for i in range(n):
        for j in range(n):
            if tube[i][j] != 0:
                virus_list.append([tube[i][j], i, j])
    
    virus_list.sort()  # 낮은 번호순으로 정렬

    new_virus = []
    for virus_num, i, j in virus_list:
        new_virus.append(trans(i, j)) # 번호 순서대로 전염 정보를 저장시킴

    for virus_group in new_virus:
        for virus_num, i, j in virus_group:
            tube[i][j] = virus_num # 결과적으로 번호가 낮은 순서대로 전염

print(tube[x-1][y-1])
