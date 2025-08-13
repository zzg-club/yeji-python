import math

a,b,v = map(int, input().split())

k = (v-b) / (a-b)
print(math.ceil(k))