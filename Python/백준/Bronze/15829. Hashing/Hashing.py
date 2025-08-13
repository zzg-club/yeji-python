r = 31
m = 1234567891
l = int(input())
target = input()

result = 0
for i in range(len(target)):
    result += (ord(target[i])-96) * (31**i)
    
print(result % m)