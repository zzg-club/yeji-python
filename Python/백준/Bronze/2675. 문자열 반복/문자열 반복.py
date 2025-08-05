t = int(input())
for _ in range(t):
    r, s = input().split()
    p = ""
    for i in s:
        for _ in range(int(r)):
            p += i
    
    print(p)