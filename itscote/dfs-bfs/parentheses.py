# 기출-18 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3

# 한쪽이 균형잡힌 문자열이 되도록 자르는 인덱스 반환
def balance(s):
    r = 0
    l = 0
    for i in range(len(s)):
        if s[i] == "(":
            r += 1
        else: 
            l += 1
        
        if r == l:
            return i+1

# 올바른 문자열인지 확인   
def correct(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1
        if count < 0:  # )가 (보다 많아질 때
            return False
    
    if count == 0:
        return True
            

def solution(p):
		# 이후에 계속 재귀적으로 호출하기 때문에 p가 빈 문자열이 되면 끝내기
    if p == "":
        return ""
        
    answer = ''
    slice_index = balance(p)
    u = p[:slice_index]
    v = p[slice_index:]
    
    # u가 올바른 문자열이면 u + 재귀적 v
    if correct(u): answer = u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        u = u[1:len(u)-1]
        new_u = ""
        for i in range(len(u)):
            if u[i] == "(": 
                new_u += ")"
            else: 
                new_u += "("
        
        answer += new_u
    
    return answer