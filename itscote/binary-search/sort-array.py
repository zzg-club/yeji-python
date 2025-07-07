# 기출 27) 정렬된 배열에서 특정 수의 개수 구하기

# n, m = map(int, input().split())

# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] += 1

# if array[m] == 0:
#     print(-1)
# else:
#     print(array[m])

# 시간 복잡도 O(logn)
# n: 원소 개수 / m: 찾으려는 수
n, m = map(int, input().split())

# 공백으로 구분된 원소들 리스트로 입력 받기
a = list(map(int, input().split()))

# array에서 target이 가장 처음 등장하는 인덱스 찾아 반환하는 함수 (없으면 -1 반환)
def search_first(array, target):
    start, end = 0, n - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid # 일단 저장
            end = mid - 1 # 왼쪽(작은 인덱스)에 더 있을 수 있으니 계속 탐색
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result

# array에서 target이 가장 마지막에 등장하는 인덱스를 찾아 반환하는 함수
def search_last(array, target):
    start, end = 0, n - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid # 일단 저장    
            start = mid + 1 # 오른쪽(큰 인덱스)에 더 있을 수 있으니 계속 탐색
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result
        
first = search_first(a, m)
last = search_last(a, m)

# 타켓 숫자가 아예 등장하지 않은 경우 first == -1
if first == -1:
    print(-1)
else:
    print(last - first + 1)