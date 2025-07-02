# 기출 28) 고정점 찾기
n = int(input())
a = list(map(int, input().split()))

def search(array):
    start, end = 0, n
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

result = search(a)

print(result)
