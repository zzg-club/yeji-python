# 치킨 배달

n, m = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

home = []     # 집의 좌표들 리스트
chicken = []  # 치킨집 좌표들 리스트

# 집의 좌표와 치킨집의 좌표를 2차원 리스트로 저장하는 루프
for row in range(n):
    for col in range(n):
        if city[row][col] == 1:
            home.append([row+1, col+1])
        elif city[row][col] == 2:
            chicken.append([row+1, col+1])

chicken_dist = [] # 각 인덱스별(치킨집)로 집과의 거리를 담을 리스트
# 예를 들면 [[치킨1-집1 거리, 치킨1-집2 거리, 치킨1-집3 거리], [치킨2-집1 거리, 치킨2-집2 거리, 치킨2-집3 거리]...]

for c in chicken:
    temp = []
    for h in home:
        temp.append(abs(h[0] - c[0]) + abs(h[1] - c[1])) # 거리 구하기
    chicken_dist.append(temp)

# 콤비네이션을 코드 로직으로 구현해보려고 했으나.. 모르겠어서 라이브러리 사용
import itertools
nCr = list(itertools.combinations(chicken_dist, m)) # 치킨거리, 즉 치킨집들 중에서 m개를 고르는 경우의 수를 리스트로

print(nCr)

result = 1000

# 총 치킨집들 중에서 m개의 치킨집만 남겨두었을 경우의 각 케이스들
for case in nCr:
    print(case)
    city_distance = 0 # 각 케이스마다 최소 도시의 치킨거리 초기화

    # 1개의 치킨집만 남겨둘 경우, 도시의 치킨거리는 해당 치킨집과 다른 집들과의 거리의 합
    if m == 1:
        city_distance = sum(case[0])
    else:
        for c in range(len(chicken) + 1):
            chicken_distance = 1000
            for i in range(m):
                if case[i][c] <= chicken_distance: chicken_distance = case[i][c]
            
            print(chicken_distance)
            city_distance += chicken_distance
    
    if result >= city_distance: result = city_distance

print(result)