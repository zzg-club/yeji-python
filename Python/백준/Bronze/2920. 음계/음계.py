num = list(map(int, input().split()))

def isasc(num):
    asc = True
    for i in range(len(num)):
        if num[i] != i+1:
            asc = False
    return asc

def isdsc(num):
    dsc = True
    for i in range(len(num)):
        if num[i] != len(num) - i:
            dsc = False
    return dsc

if isasc(num):
    print("ascending")
elif isdsc(num):
    print("descending")
else:
    print("mixed")