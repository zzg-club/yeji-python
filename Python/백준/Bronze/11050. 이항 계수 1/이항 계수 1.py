n,k = map(int, input().split())

def fac(k):
    if k == 0:
        return 1
    return k * fac(k-1)

result = fac(n) // (fac(k) * fac(n - k))
print(result)