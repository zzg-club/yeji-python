# 문자열 재정렬

s = input()

num = 0          # 숫자 문자열들을 더해줄 변수
str_list = []    # 문자들을 저장할 리스트

# 아스키코드가 47 초과 58 미만이라면(숫자) int로 변환 후 num에 더한다
# 문자들은 str_list에 저장
for chr in s:
    if 47 < ord(chr) < 58:
        num += int(chr)
    else:
        str_list.append(chr)

# 오름차순 정렬한 str_list를 문자열로 변환 + num을 문자열로 변환
result = ''.join(sorted(str_list)) + str(num)

print(result)