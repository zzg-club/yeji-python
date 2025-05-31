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

# 문제 조건에 맞는 사칙연산 함수
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0:
            return -(-a // b)
        else:
            return a // b

# 모든 순열 경우의 수에 따른 연산 결과를 담을 배열
result = []

# 순열 케이스들을 순회하며 연산 후 결과 리스트에 저장
for case in op_perm:
    res = num[0]
    for i in range(len(case)):
        res = calc(res, num[i+1], case[i])
    result.append(res)

print(max(result))
print(min(result))