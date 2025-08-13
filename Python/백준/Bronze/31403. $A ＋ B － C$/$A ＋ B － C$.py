str_list = []
for _ in range(3):
    str_list.append(input())
    
num_result = int(str_list[0])+int(str_list[1])-int(str_list[2])
str_result = int(str_list[0]+str_list[1])-int(str_list[2])

print(num_result)
print(str_result)