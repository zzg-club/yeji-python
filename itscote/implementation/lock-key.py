# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059


# 오른쪽으로 열쇠를 회전한 뒤 해당 좌표 리스트를 반환하는 함수
def turn_right(key):
    m = len(key)
    turn_key = [[0]*m for _ in range(m)] # 리스트 컴프리헨션
    for r in range(m):
        for c in range(m):
            # 열의 원소가 행의 원소가 되고, m-1에서 현재 행을 뺀 수가 열이 됨
            turn_key[c][m-r-1] = key[r][c]
    return (turn_key)
        
# 자물쇠의 홈 좌표들을 모아 리스트로 반환하는 함수
def home_coord(lock):
    n = len(lock)
    home = []
    for r in range(n):
        for c in range(n):
            if lock[r][c] == 0:
                home.append([r,c])
    return home

# 열쇠의 돌기 좌표들을 모아 리스트로 반환하는 함수
def key_coord(key):
    n = len(key)
    prot = []
    for r in range(n):
        for c in range(n):
            if key[r][c] == 1:
                prot.append([r,c])
    return prot

def move(prot, dr, dc):
    # [[x, y], [x, y], ...] 형태의 prot의 각 원소들에 dr, dc를 더함
    # 열쇠를 동서남북 모든 조합으로 한칸 씩 이동하는 함수
    return [[r + dr, c + dc] for r, c in prot]

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    lock_home = home_coord(lock) # 자물쇠의 홈 좌표들 리스트
    
    for _ in range(4):
        key = turn_right(key)       # 열쇠를 오른쪽으로 회전
        key_prot = key_coord(key)   # 회전한 열쇠의 돌기 좌표들 리스트
    
        # 열쇠 크기 < 자물쇠 크기이므로 열쇠의 돌기 좌표들을 자물쇠 크기만큼 상하좌우로 움직이는 루프
        for dr in range(-n + 1, n):      # 상하 움직임
            for dc in range(-n + 1, n):  # 좌우 움직임
                moved_key = move(key_prot, dr, dc)  # 열쇠 돌기를 움직인 좌표 값 리스트

                # moved_key의 좌표들이 lock_home의 좌표들과 일치하면 True
                match = True
                for home in lock_home:
                    if home not in moved_key:
                        match = False
                        break
                        
                if match: return True
                        
    
    return False