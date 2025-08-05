a = int(input())
b = int(input())
c = int(input())

r = a * b * c
howmany = [0] * 10
for s in str(r):
    howmany[int(s)] += 1
    
for h in howmany:
    print(h)