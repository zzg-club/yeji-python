# 실전 03) 개미 전사

n = int(input())
food = list(map(int, input().split()))

# d[i] : food의 인덱스 [i]까지 얻을 수 있는 최대 식량값
d = [0] * 101

# food[0]까지의 최댓값은 food[0]
d[0] = food[0]
# food[1]까지의 최댓값은 food[0] or food[1]
d[1] = max(food[0], food[1])

# ex. food[2]까지의 최댓값은 
# d[1](food[1]까지의 최댓값, food[2]는 건너뜀) 
# or d[0] + food[2](food[0]까지의 최댓값 + 현재 창고의 식량값)
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+food[i])

# 마지막 인덱스까지 dp 후 출력
print(d[n-1])