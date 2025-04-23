# 무지의 먹방 라이브

def solution(food_times, k):
    n = len(food_times)
    idx = 0
    for i in range(k):
        count = 0
        while food_times[idx] == 0:
            if idx == n-1: idx = 0
            else: idx += 1
            count += 1
        
        food_times[idx] -= 1
            
        if count == n:
            return -1
            
        if idx == n-1: idx = 0
        else: idx += 1
    
    count = 0
    while food_times[idx] == 0:
        if idx == n-1: idx = 0
        else: idx += 1
        count += 1
        if count == n:
            return -1
        
    return idx + 1