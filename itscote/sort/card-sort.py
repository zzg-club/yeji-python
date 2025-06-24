# 기출 26) 카드 정렬하기
# https://www.acmicpc.net/problem/1715

n = int(input())
cards = [int(input()) for _ in range(n)]

total = 0

while len(cards) > 1:
    cards.sort()  # 항상 정렬
    a = cards.pop(0)
    b = cards.pop(0)
    cost = a + b
    total += cost
    cards.append(cost)

print(total)