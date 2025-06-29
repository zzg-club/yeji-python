# 실전 3) 떡볶이 떡 만들기

n, m = map(int, input().split())
tteok = list(map(int, input().split()))

def cut(mid):
    result = 0
    for t in tteok:
        if t > mid:
            result += t - mid
    return result

def search(array, target, start, end):
    result = 0
    while (start <= end):
        mid = (start + end) // 2
        if cut(mid) == target:
            return mid
        elif cut(mid) > target: # 최대 높이를 구하는 것이므로 일단 result로 기록해두고 더 높이기
            result = mid
            start = mid + 1
        else: # 부족하면 mid를 더 낮춰서 많이 자름
            end = mid - 1
            

result = search(tteok, m, 0, max(tteok))

print(result)

# ----------------------------------------
# 교재 답안
n, m = list(map(int, input().split(' ')))
array  list(map(int, input().spit()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid + 1
    
print(result)