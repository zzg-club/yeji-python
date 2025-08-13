t = int(input())

for _ in range(t):
    k = int(input())  # 층
    n = int(input())  # 호수

    apt = [[0]*(n+1) for _ in range(k+1)]

    for j in range(1, n+1):
        apt[0][j] = j

    for i in range(1, k+1):
        for j in range(1, n+1):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]

    print(apt[k][n])
