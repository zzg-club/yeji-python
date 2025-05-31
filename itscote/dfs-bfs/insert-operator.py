# 기출-19 연산자 끼워 넣기
#  https//www.acmicpc.net/problem/14888

import itertools

n = int(input())
num = list(map(int, input().split()))
op_info = list(map(int, input().split()))
op_type = ['+', '-', '*', '/']

# op_info와 op_type을 통해 입력받은 연산자를 모두 op 배열에 넣음
op = []
for i in range(len(op_info)):
    for j in range(op_info[i]):
        op.append(op_type[i])
    
# 입력받은 연산자의 모든 순열 조합
nPr = itertools.permutations(op, len(op))
op_perm = list(nPr)


result = []

for case in op_perm:
    exp = []
    for i in range(len(case)):
        exp.append(str(num[i]))
        exp.append(case[i])
    
    exp.append(str(num[-1]))
    str_exp = ''.join(exp)
    result.append(eval(str_exp))

print(max(result))
print(min(result))