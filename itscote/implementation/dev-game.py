# 게임 개발


# NxM 맵 생성
n, m = map(int, input().split())
# 캐릭터의 초기 위치 (a,b,방향) - a: y축 인덱스 / b: x축 인덱스
a, b, d = map(int, input().split())
# 맵 정보 0: 육지 / 1: 바다
map_info = []
for column in range(n):
    map_info.append(list(map(int, input().split())))

# 북: 서쪽으로 회전 후 전진 / 동: 북쪽으로 회전 후 전진
# 남: 동쪽으로 회전 후 전진 / 서: 남쪽으로 회전 후 전진
nxt_step = [(0, -1, 3), (-1, 0, 0), (0, 1, 1), (1, 0, 2)]

# 뒤로가기
back_step = [(1, 0, 0), (0, -1, 1), (-1, 0, 2), (0, 1, 3)]

count = 1
turn = 0

while True:
    if map_info[a + nxt_step[d][0]][b + nxt_step[d][1]] == 0:
        map_info[a][b] = 1 # 가 봤으면 1로 바꾸기
        a += nxt_step[d][0]
        b += nxt_step[d][1]
        # d = nxt_step[d][2]
        print(a, b)
        count += 1
        turn = 0
    elif turn == 4:
        a += back_step[d][0]
        b += back_step[d][1]
        if map_info[a][b] == 1: break
    else:
        d = nxt_step[d][2]
        turn += 1

print(count)

# --------------------------------------------

# 2번쨰 풀이

# NxM 맵 생성
n, m = map(int, input().split())
# 캐릭터의 초기 위치 (a,b,방향) - a: y축 인덱스 / b: x축 인덱스
a, b, d = map(int, input().split())
# 맵 정보 0: 육지 / 1: 바다
map_info = []
for column in range(n):
    map_info.append(list(map(int, input().split())))

# 왼쪽으로 돌기
turn_left = [3, 0, 1, 2]

# 앞으로 전진
go_forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 뒤로가기
back_step = [(1, 0, 0), (0, -1, 1), (-1, 0, 2), (0, 1, 3)]

count = 1
turn = 0

while True:
    d = turn_left[d]
    turn += 1

    if map_info[a + go_forward[d][0]][b + go_forward[d][1]] == 0:
        map_info[a][b] = 1 # 가 봤으면 1로 바꾸기
        a += go_forward[d][0]
        b += go_forward[d][1]
        print(a, b)
        count += 1
        turn = 0
    elif turn == 4:
        a += back_step[d][0]
        b += back_step[d][1]
        if map_info[a][b] == 1: break

print(count)


# --------------------------------------------

# 교재 풀이

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d =[[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)