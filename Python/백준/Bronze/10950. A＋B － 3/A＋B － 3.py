n = int(input())
tc = [list(map(int, input().split())) for _ in range(n)]

for a,b in tc:
    print(a+b)