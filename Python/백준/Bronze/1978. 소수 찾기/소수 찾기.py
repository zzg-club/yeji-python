n = int(input())
num = list(map(int, input().split()))

result = 0
for t in num:
    p = True
    if t > 1:
        for i in range(2, t):
            if t % i == 0:
                p = False
    
        if p:
            result += 1
        
print(result)