# 기출 24) 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
home = list(map(int, input().split()))

def dist(an):
    dist = 0
    for i in range(n):
        dist += abs(an - home[i])
    return dist

result = float("inf")
loc = 0

for i in range(n):
    an = home[i]
    if result > dist(an):
        result = dist(an)
        loc = an

print(loc)