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