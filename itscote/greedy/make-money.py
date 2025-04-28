# 만들 수 없는 금액

n = int(input())
coin_list = list(map(int, input().split())) # 주어진 동전을 리스트로 받음

import itertools

# 동전으로 만들 수 있는 모든 조합을 구한 리스트 1개 ~ n개
coin_comb = []
for i in range(1, len(coin_list)):
    coin_comb.append(list(itertools.combinations(coin_list, i)))

# print(coin_comb)

# 각 경우의 수 당 만들 수 있는 최종 금액 리스트
coin_sum = []
for case in coin_comb:
    for each in case:
        coin_sum.append(sum(each))

# 중복된 원소 제거를 위해 set으로 만들었다가, 다시 리스트로 만듦
coin_set = set(coin_sum)
# print(coin_set)
coin_case = list(coin_set)

# 중복된 원소가 제거된 리스트를 오름차순 정렬
coin_case.sort()

# 1부터 coin_case의 길이 만큼 루프를 돌면서 1부터 모든 수가 있는지 확인
# 없다면, 모든 경우의 수를 따져도 해당 수를 만들 수 없는 것이므로 print 후 break
for i in range(1, len(coin_case)):
    if i == coin_case[i-1]:
        continue
    else:
        print(i)
        break