# 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
    ext_weak = [] # 원형 -> 직선 확장
    for point in weak:
        ext_weak.append(point) # 해당 위치와 확장한 위치를 추가
        ext_weak.append(n + point)
    
    ext_weak.sort() # 오름차순 정렬
    
    # 배치할 친구들의 순서들의 모든 경우의 수 (순열)
    # ex. [1,2,3], [1,3,2] [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    perm = list(permutations(dist))
    
    result = 999 # result 큰 수로 초기화
    
    # 친구 배치 순서 경우의 수를 for루프로 돌면서 확인
    for friends in perm:
        # 첫번째 for루프: 첫번째 순서 친구를 어느 취약점에 배치할 것인지
        for i in range(len(weak)):
            fcount = 1                         # 투입한 친구 수
            loc = ext_weak[i] + friends[0]     # 투입한 친구가 확인을 마친 위치 (포인터 같은 역할)
            
            # 두번째 for루프: 그 다음 취약점을 현재 친구가 확인 가능한지
            for j in range(i + 1, i + len(weak)):
                # 첫번째 루프에서 첫 친구가 두번째 취약점까지 확인하지 못했을 경우
                if loc < ext_weak[j]:
                    fcount += 1 # 한 명 더 투입
                    
                    if fcount >= len(dist):  # 친구 초과
                        break
                    else: # 친구 투입 가능할 경우, 그 다음 취약점에 배치
                        loc = ext_weak[j] + friends[fcount - 1]
            
            # 친구 초과하지 않았을 경우, result와 비교하여 최소찾기
            if fcount <= len(dist):
                result = min(result, fcount)
            
    # 만약 친구 초과할 경우(result 갱신 안됨) -> return -1            
    if result >= len(dist):
        result = -1
    
    return result