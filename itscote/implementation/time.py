# 시간

n = int(input())

h, m, s = 0, 0, 0

count = 0

for hour in range(n+1):
    m = 0
    for minute in range(60):
        s = 0
        for second in range(60):
            s += 1
            # if '3' in str(s) or '3' in str(m) or '3' in str(h): 
            #     count += 1
            if '3' in str(s): count += 1
            elif '3' in str(m): count += 1
            elif '3' in str(h): count += 1 
        m += 1
    h += 1
    

print(count)

# --------------------------------------------

# 교재 답안

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)