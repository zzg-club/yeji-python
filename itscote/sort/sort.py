array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 왼쪽 데이터가 자기보다 크면 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에 멈춤
            break

print(array)

# 퀵 정렬 (직관적)
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        #  피벗보다 큰 데이터를 찾을 떄까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 답고 있다면 종료
        if len(array) <= 1:
            return array

        pivot = array[0] # 피벗은 첫 번째 원소
        tail = array[1:] # 피벗을 제외한 리스트

        left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
        right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

