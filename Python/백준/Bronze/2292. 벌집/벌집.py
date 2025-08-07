n = int(input())

k = 1
m = 1
result = 1
while True:
    if n <= k:
        print(m)
        break
    else:
        k += 6 * m
        m += 1