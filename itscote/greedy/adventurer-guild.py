# 모험가 길드

n = int(input())
level_list = list(map(int, input().split()))

level_list.sort(reverse=True) # 내림차순 정렬

index = 0
group_count = 0

while index < n:
    group_count += 1
    index += level_list[index]

print(group_count)