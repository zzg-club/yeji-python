# 럭키 스트레이트

n = input()

half = len(n) // 2

left, right = 0, 0

for i in range(half):
    left += int(n[i])
    right += int(n[len(n) - 1 - i])

# print(left, right)

if left == right:
    print("LUCKY")
else:
    print("READY")