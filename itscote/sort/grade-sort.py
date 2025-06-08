# 실전3) 성적이 낮은 순서로 학생 출력하기

n = int(input())
grade = [input().split() for _ in range(n)]

grade.sort(key=lambda x:int(x[1]))

for name, score in grade:
    print(name, end=' ')