# 기출-23 국영수
# https://www.acmicpc.net/problem/10825

n = int(input())
score = [input().split() for _ in range(n)]

score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name, ko, en, math in score:
    print(name)