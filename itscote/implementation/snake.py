# 뱀

n = int(input()) # 정사각형 보드 크기

k = int(input()) # 사과 개수
apple = [] # 사과 좌표 리스트
for i in range(k):
    apple.append(list(map(int, input().split())))

d = int(input()) # 방향 변환 횟수
direction = [] # 방향 전환 정보 리스트
for i in range(d):
    direction.append(list(map(str, input().split()))) # str 형태임

# print(apple)
# print(direction)

snake = [[1,1]] # 뱀의 몸이 차지하는 좌표들
d_now = 1 # 현재 뱀의 방향 0: 북 1: 동 2: 남 3: 서

count = 0 # 초

def go():
    go_list_r = [-1, 0, 1, 0]
    go_list_c = [0, 1, 0, -1]

    return [snake[-1][0] + go_list_r[d_now], snake[-1][1] + go_list_c[d_now]]

while True:

    nxt = go()
    count += 1

    # 자신의 몸과 부딪히는 경우
    if nxt in snake:
        break

    # 벽에 부딪히는 경우
    if not (1 <= nxt[0] <= n and 1 <= nxt[1] <= n):
        break
        
    snake.append(nxt)

    # 사과가 없는 경우 꼬리 없애기
    if nxt not in apple:
        snake.pop(0)

    for d_info in direction:
        if count == int(d_info[0]): 
            if d_info[1] == 'D':
                d_now = (d_now + 1) % 4
            else:
                d_now = (d_now + 3) % 4

print(count)