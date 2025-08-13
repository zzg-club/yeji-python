h, m = map(int, input().split())

if m < 45:
    m = 60 - (45 - m)
    if h == 0:
        h = 23
    else:
        h = h - 1
else:
    m = m - 45
    
print(f"{h} {m}")