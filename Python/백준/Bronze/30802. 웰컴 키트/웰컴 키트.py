import math

n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

sorder = []
for s in shirts:
    sorder.append(math.ceil(s/t))
    
print(sum(sorder))
print(f"{n//p} {n%p}")