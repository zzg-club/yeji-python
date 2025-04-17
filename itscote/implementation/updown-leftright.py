# 상하좌우

n = int(input()) # 공간의 크기
move_plan = list(input().split())

loc = [1, 1]

for move in move_plan:
    if move == "R":
        loc[1] += 1
    elif move == "L":
        loc[1] -= 1
    elif move == "U":
        loc[0] -= 1
    elif move == "D":
        loc[0] += 1

    if loc[0] < 1: loc[0] = 1
    elif loc[0] > n: loc[0] = n
    elif loc[1] < 1: loc[1] = 1
    elif loc[1] > n: loc[1] = n

print(*loc) # 대괄호 없이 한번에 출력 가능


# --------------------------------------------

# 교재 답안

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)