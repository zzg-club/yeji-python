# 미로 탈출

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

from collections import deque

def bfs(x,y):
    count = 0
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))


    print(maze[n-1][m-1])    

bfs(0,0)