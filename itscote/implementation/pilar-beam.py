# 기둥과 보
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# 설치 가능한지 여부 판단 함수
def install(step, answer):
    x, y, t = step
    
    if t == 0:  # 기둥
        if not (y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer):
            return False
    else: # 보
        if not ([x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer)):
            return False
    return True

# 삭제 가능한지 여부 판단 함수
def delete(step, answer):
    x, y, t = step
    answer.remove([x, y, t]) # 해당 기둥/보 먼저 삭제

    # 삭제 시 나머지가 규칙을 만족하는지 확인
    for a in answer:
        ax, ay, at = a
        if at == 0: # 기둥
            if not (ay == 0 or [ax, ay-1, 0] in answer or [ax-1, ay, 1] in answer or [ax, ay, 1] in answer):
                answer.append([x, y, t])
                return False
        else: # 보
            if not ([ax, ay-1, 0] in answer or [ax+1, ay-1, 0] in answer or ([ax-1, ay, 1] in answer and [ax+1, ay, 1] in answer)):
                answer.append([x, y, t])
                return False

    answer.append([x,y,t])
    return True
    
def solution(n, build_frame):
    answer = []
    
    for step in build_frame:
        x = step[0]
        y = step[1]
        t = step[2]
        
        # 설치
        if step[3] == 1:
            if install([x, y, t], answer):
                answer.append([x, y, t])
        # 삭제
        else:
            if [x, y, t] in answer:
                if delete([x, y, t], answer):
                    answer.remove([x, y, t])
                
    answer.sort()
    
    return answer