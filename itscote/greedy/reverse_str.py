# 문자열 뒤집기

s = input()

zero = 0
one = 0

for i in range(len(s)):
    if (i == 0 or s[i] != s[i-1]):
        if s[i] == '0': zero += 1
        else: one += 1

# 0 -> 1로 바뀌는 순간을 통해 0이 연속해서 나오는 횟수를 카운트 = zero
# 1 -> 0으로 바뀌는 순간을 통해 1이 연속해서 나오는 횟수를 카운트 = one
# i번째 인덱스와 i-1번째 인덱스를 비교하므로 0번째 인덱스는 무조건 카운트

result = min(zero, one)

print(result)