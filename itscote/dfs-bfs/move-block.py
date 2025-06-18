# 기출 22) 블록 이동하기
# https://school.programmers.co.kr/learn/courses/30/lessons/60063?language=python3

from collections import deque

move_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌

def move(pos, d, board):
    dx1 = pos[0][0] + move_dir[d][0]
    dy1 = pos[0][1] + move_dir[d][1]
    dx2 = pos[1][0] + move_dir[d][0]
    dy2 = pos[1][1] + move_dir[d][1]

    n = len(board)
    if 0 <= dx1 < n and 0 <= dy1 < n and 0 <= dx2 < n and 0 <= dy2 < n:
        if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
            return [[dx1, dy1], [dx2, dy2]]
    return None

def turn(pos, board):
    result = []
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    n = len(board)

    if x1 == x2:  # 가로방향
        for d in [-1, 1]:
            if 0 <= x1 + d < n and 0 <= x2 + d < n:
                if board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                    result.append([[x1, y1], [x1 + d, y1]])
                    result.append([[x2, y2], [x2 + d, y2]])
    elif y1 == y2:  # 세로방향
        for d in [-1, 1]:
            if 0 <= y1 + d < n and 0 <= y2 + d < n:
                if board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                    result.append([[x1, y1], [x1, y1 + d]])
                    result.append([[x2, y2], [x2, y2 + d]])
    return result

def solution(board):
    n = len(board)
    visited = set()
    start = [[0, 0], [0, 1]]
    q = deque()
    q.append((start, 0))
    visited.add(tuple(sorted(tuple(p) for p in start)))

    while q:
        pos, cost = q.popleft()
        if [n - 1, n - 1] in pos:
            return cost

        # 4방향 이동
        for i in range(4):
            moved = move(pos, i, board)
            if moved:
                moved_key = tuple(sorted(tuple(p) for p in moved))
                if moved_key not in visited:
                    visited.add(moved_key)
                    q.append((moved, cost + 1))

        # 회전
        for rotated in turn(pos, board):
            rotated_key = tuple(sorted(tuple(p) for p in rotated))
            if rotated_key not in visited:
                visited.add(rotated_key)
                q.append((rotated, cost + 1))

    return 0
