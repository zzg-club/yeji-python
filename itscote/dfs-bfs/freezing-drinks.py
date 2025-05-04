# 음료수 얼려 먹기

n, m = map(int, input().split())
mold = [list(map(int, input())) for _ in range(n)]

def check(r, c):
    # n, m의 범위를 벗어나면 끊어주기
    if not (0 <= r < n and 0 <= c < m):
        return False
    
    # 해당 위치가 0이면 1로 방문처리
    if mold[r][c] == 0:
        mold[r][c] = 1
        check(r-1, c) # 상하좌우를 체크
        check(r+1, c)
        check(r, c-1)
        check(r, c+1)
        return True

    return False

result = 0

for r in range(n):
    for c in range(m):
        if check(r, c):
            result += 1

print(result)
