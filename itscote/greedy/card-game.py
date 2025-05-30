# 숫자 카드 게임

# n = 행의 개수, m = 열의 개수
n, m = map(int, input().split())

min = 0

for i in range(n):
    row = list(map(int, input().split()))
    row.sort() # 오름차순 정렬

    if (min < row[0]): min = row[0] # 행의 최솟값들을 비교

print(min)

# --------------------------------------------

# 교재 풀이 - min() 함수 사용

# N, M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
	data = list(map(int, input().split()))
	# 현재 줄에서 '가장 작은 수' 찾기
	min_value = min(data)
	# '가장 작은 수'들 중에서 가장 큰 수 찾기
	result = max(result, min_value)
	
print(result)

# --------------------------------------------

# 2중 반복문 구조 사용

# N, M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
	data = list(map(int, input().split()))
	# 현재 줄에서 '가장 작은 수' 찾기
	min_value = 10001
	for a in data:
		min_value = min(min_value, a)
	# '가장 작은 수'들 중에서 가장 큰 수 찾기
	result = max(result, min_value)

print(result) # 최종 답안 출력