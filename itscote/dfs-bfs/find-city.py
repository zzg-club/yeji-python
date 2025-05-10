# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

n, m, k, x = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(m)]

# answer = []
# visited = [False] * (n + 1)

# def dfs(city, count):
#     visited[city] = True
#     if count == k:
#         if city not in answer:
#             answer.append(city)
#         return
    
#     for r in road:
#         if r[0] == city and not visited[r[1]]:
#             dfs(r[1], count + 1)
    
#     visited[city] = False 

# dfs(x, 0)
# answer.sort()

# if answer:
#     for city in answer:
#         print(city)
# else:
#     print(-1)

from collections import deque

visited = [False] * (n + 1) # 방문 여부
distance = [0] * (n + 1) # 출발점으로부처의 각 거리
answer = []

queue = deque()
queue.append(x) # 출발 도시를 큐에 넣음
visited[x] = True # x번째 인덱스 방문처리

while queue:
    city = queue.popleft()
    
    if distance[city] == k: # 현재 도시까지 거리가 k이면 answer 리스트에 넣기
        answer.append(city)
        continue # 탐색 중단
    
    for r in road: # 다음 도시로 이동
        if r[0] == city and not visited[r[1]]: # 현재 도시와 연결되어 있고, 방문하지 않은 곳일때
            visited[r[1]] = True # 방문 처리
            distance[r[1]] = distance[city] + 1 # 거리 누적 (이전거리 + 1)
            queue.append(r[1]) # 큐에 넣음

if answer:
    answer.sort()
    for city in answer:
        print(city)
else:
    print(-1)