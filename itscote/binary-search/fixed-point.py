# 기출 28) 고정점 찾기
# 고정점 = 원소 값이 인덱스와 동일한 원소

# 원소의 개수 n
n = int(input())

# 공백으로 구분된 수열 리스트로 입력 받기
a = list(map(int, input().split()))

# 리스트를 인자로 받아 고정점을 찾아 리턴하는 함수 (없으면 -1 리턴)
def search(array):
    start, end = 0, n
    while start <= end:
        mid = (start + end) // 2 # 중간부터 탐색 (mid = 탐색할 인덱스)
        if array[mid] == mid: # 원소값이 인덱스값과 같으면 해당 인덱스(mid) 리턴
            return mid
        elif array[mid] > mid: # 인덱스보다 원소값이 크면 더 작은 인덱스 탐색 (왜냐면 수열이 이미 정렬된 상태이기 때문에 큰 인덱스의 원소값들은 이미 인덱스값보다 숫자가 클 것)
            end = mid - 1
        else: # 인덱스보다 원소값이 작다면 더 큰 인덱스 탐색
            start = mid + 1 
    return -1 # 고정점을 찾지 못하고 탐색을 마친 경우 -1 리턴

result = search(a)

print(result)
