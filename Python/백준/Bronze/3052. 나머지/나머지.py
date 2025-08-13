n = []
for _ in range(10):
    num = int(input())
    n.append(num % 42)
    
result = list(set(n))
print(len(result))