# 실전 2) 부품 찾기

n = int(input())
whole = list(map(int, input().split()))
m = int(input())
parts = list(map(int, input().split()))

def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for part in parts:
    if search(whole, part, 0, n-1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# ----------------------------------------
#  계수 정렬 (교재 답안)
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))
# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# ----------------------------------------
#  집합 자료형 (교재 답안)
# N(가게의 부품 개수)을 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x：
    # 해당 부품이 존재하는지 확인
    if i in array：
        print('yes', end=' ')
    else：
        print('no', end=' ')