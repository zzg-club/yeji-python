# 볼링공 고르기

n, m = map(int, input().split())
weight_list = list(map(int, input().split()))

same = 0 # 같은 수를 뽑는 경우의 수 * 2

for i in range(n):
    count = weight_list.count(weight_list[i])
    # print('i=', i, '//', weight_list[i], ':', count)
    if count > 1:
        same += count * (count-1) // 2


result = n * (n-1) // 2 - same // 2

# 전체 개수에서 2개 뽑는 경우의 수 - 같은 무게의 공을 2개 뽑는 경우의 수

print(result)