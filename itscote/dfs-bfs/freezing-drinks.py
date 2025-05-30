# 음료수 얼려 먹기

n, m = map(int, input().split())
mold = [list(map(int, input())) for _ in range(n)]

def check(r, c):
    # n, m의 범위를 벗어나면 끊어주기
    if not (0 <= r < n and 0 <= c < m):
        return False
    
    # 해당 위치가 0이면 1로 방문처리
    if mold[r][c] == 0:
        mold[r][c] = 1
        check(r-1, c) # 상하좌우를 체크
        check(r+1, c)
        check(r, c-1)
        check(r, c+1)
        return True

    return False

result = 0

for r in range(n):
    for c in range(m):
        if check(r, c):
            result += 1

print(result)


# --------------------------------------------

# 교재 풀이

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
		graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
		# 주어진 범위를 벗어나는 경우에는 즉시 종로
		if x <= -1 or x >= n or y <= -1 or y >= m:
				return False
		# 현재 노드를 아직 방문하지 않았다면
		if graph[x][y] == 0:
				# 해당 노드 방문 처리
				graph[x][y] = 1
				# 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
				dfs(x-1, y)
				dfs(x, y-1)
				dfs(x+1, y)
				dfx(x, y+1)
				return True
		return False
		
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
		for j in range(m):
				# 현재 위치에서 DFS 수행
				if dfs(i,j) == True:
						result += 1
						
print(result) # 정답 출력