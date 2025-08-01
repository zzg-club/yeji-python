num = [int(input()) for _ in range(9)]

maxnum = -1
index = -1
for i in range(9):
    if num[i] > maxnum:
        maxnum = num[i]
        index = i + 1
        
print(maxnum)
print(index)