n = int(input())

for i in range(1, n+1):
    si = list(map(int, str(i)))
    if n == i + sum(si):
        print(i)
        break
    if i == n:
        print(0)