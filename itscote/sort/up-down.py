# 실전2) 위에서 아래로

n = int(input())
num = [int(input()) for _ in range(n)]

num.sort(reverse=True)

for i in range(n):
    print(num[i], end=' ')