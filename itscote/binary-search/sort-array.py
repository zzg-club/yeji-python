# 기출 27) 정렬된 배열에서 특정 수의 개수 구하기

n, m = map(int, input().split())

array = [0] * 1000001

for i in input().split():
    array[int(i)] += 1

if array[m] == 0:
    print(-1)
else:
    print(array[m])