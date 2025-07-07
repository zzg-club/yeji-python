# 기출 29) 공유기 설치
# https://www.acmicpc.net/problem/2110

# n: 집의 개수 / c: 설치할 공유기의 개수
n,c = map(int, input().split())

# 줄마다 입력되는 집의 좌표를 리스트로 입력 받기
home = [int(input()) for _ in range(n)]
home.sort() # 집의 좌표들 오름차순 정렬

# 두 집 사이의 거리가 최소 dist일 때, c개의 공유기가 설치 가능한지 확인하는 함수
def install(dist):
    prev = home[0] # 무조건 첫번째 집에 공유기 설치
    count = 1 # 첫번째 집에 공유기 설치했으므로 설치한 공유기의 수 = 1

    # 인덱스 i를 통해 home을 순회하면서 dist보다 큰 간격으로 공유기 설치
    for i in range(1, len(home)):
        if home[i] - prev >= dist: # 현재 위치(home[i])와 이전 공유기 위치(prev) 사이의 거리가 dist보다 클 경우
            count += 1 # 공유기 설치
            prev = home[i] # 이전 공유기 위치를 현재 위치로 갱신
    
    # 만약 지금까지 설치한 공유기 개수(count)가 설치해야하는 공유기 개수(c)보다 크면 설치 가능 True
    if count >= c: return True
    return False

# home 리스트를 인자로 받아 공유기를 어떤 간격으로 배치할지 결정하는 함수
# home 리스트가 전역변수이기 때문에 사실 굳이 매개변수로 쓸 이유는 없지만.. 
def search(home):
    # 여기서 start, end는 "공유기를 설치할 집 사이의 간격" (dist)를 의미
    start = 1 # 최소 간격은 1
    end = home[-1] - home[0] # 최대 간격은 첫 집과 마지막 집 사이의 거리
    result = 0 # 설치 가능한 간격 값을 저장할 변수

    while start <= end:
        mid = (start + end) // 2 # 공유기를 가장 적당한 간격으로 설치하기 위해서 가능한 간격들 중 절반에서 시작
        if install(mid):
            result = mid # 해당 간격으로 c개의 공유기가 설치 가능하다면 result에 저장
            start = mid + 1 # 더 큰 간격으로도 가능한지 확인
        else:
            end = mid - 1 # 해당 간격으로 c개의 공유기가 설치 불가능하다면 간격을 줄임
    
    return result

print(search(home))