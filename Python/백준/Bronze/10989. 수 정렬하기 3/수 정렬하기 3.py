import sys
input = sys.stdin.readline

# 계수정렬
n = int(input())
arr = [0] * (10000 + 1)

# 각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1
  
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)