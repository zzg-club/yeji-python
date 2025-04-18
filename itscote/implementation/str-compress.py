# 문자열 압축

s = input()

slice_list = []     # 0~문자열/2 길이 만큼 자른 단위들을 리스트에 넣음
count = 1           # 같은 문자열이 반복되는 횟수 카운트
compress_str = ""   # 최종 압축된 문자열
result = 1000       # 최종 압축된 문자열 길이

half = len(s) // 2

# 1개 단위로 자르기, 2개 단위로 자르기 , ... , 문자열 길이의 절반 단위로 자르기
for i in range(1, half + 1):
    slice_list = []

    # i개 단위로 잘라서 slice_list에 넣기
    for j in range(len(s) // i):
        slice_list.append(s[i*j:i*(j+1)])
        # print(slice_list)

    # i개 단위로 잘랐을 때 남는 덩어리 append
    rem = len(s) % i
    if rem != 0:
        slice_list.append(s[-rem:])
    
    # slice_list를 순회하면서 연속적으로 중복되는게 있는지 검사
    for k in range(len(slice_list) - 1):
        # print(str(k) + "k: " + slice_list[k] + " , k+1: " + slice_list[k+1])

        # 연속되는 원소가 중복되는 경우 연속중복횟수 count += 1
        if slice_list[k] == slice_list[k+1]:
            count += 1
        else:
            if count == 1: # 연속 중복이 아닌 경우 중 count가 1인 경우
                compress_str += slice_list[k]
            else: # 연속 중복이 아닌 경우 중 count가 1이 아닌 경우 (연속 중복 원소들이 출현하다가 다른 원소로 넘어갈 경우)
                compress_str += str(count) + slice_list[k]
                count = 1
        
    # 마지막 원소 처리.. (k와 k+1을 비교하므로 마지막 원소인 k+1은 남겨짐)
    if count == 1:
        compress_str += slice_list[-1]
    else:
        compress_str += str(count) + slice_list[-1]
        count = 1

    # result보다 현재 단위로 압축한 문자열의 길이가 짧으면 result를 대체
    if result >= len(compress_str):
        result = len(compress_str)
    
    print(compress_str)
    compress_str = ""
    

print(result)