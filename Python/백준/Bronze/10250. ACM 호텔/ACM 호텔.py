import math

t = int(input())
tc = [list(map(int, input().split())) for _ in range(t)]

for h, w, n in tc:
    floor = n % h
    if floor == 0:
        floor = h
    room = math.ceil(n / h)
    if room < 10 :
        room = "0"+str(room)
    print(f"{floor}{room}")