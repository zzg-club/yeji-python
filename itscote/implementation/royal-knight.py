# 왕실의 나이트

loc = input()
x = ord(loc[0])
y = int(loc[1])

count = 0

# 좌우로 먼저 이동
if 99 <= x <= 102:
    if 2 <= y <= 7:
        count += 4
    else:
        count += 2
else:
    if 2 <= y <= 7:
        count += 2
    else:
        count += 1

# 상하로 먼저 이동
if 3 <= y <= 6:
    if 98 <= x <= 103:
        count += 4
    else:
        count += 2
else:
    if 98 <= x <= 103:
        count += 2
    else:
        count += 1
        
print(count)

# --------------------------------------------

# 교재 답안

# 현재 나이트 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for steps in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= -1 and next_column <= 8:
        result += 1

print(result)