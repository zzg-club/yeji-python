from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

c = list(combinations(card, 3))

max_sum = 0
for cc in c:
    if sum(cc) <= m:
        max_sum = max(max_sum, sum(cc))


print(max_sum)
