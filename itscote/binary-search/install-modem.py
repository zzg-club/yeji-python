# 기출 29) 공유기 설치
# https://www.acmicpc.net/problem/2110
n,c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

def install(dist):
    prev = home[0]
    count = 1
    for i in range(1, len(home)):
        if home[i] - prev >= dist:
            count += 1
            prev = home[i]
    
    if count >= c: return True
    return False

def search(home, c):
    start = 1
    end = home[-1] - home[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if install(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

print(search(home, c))