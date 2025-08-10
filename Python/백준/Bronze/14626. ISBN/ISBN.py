isbn = input()

total = 0
damage_index = 0
for i in range(len(isbn)):
    if isbn[i] == '*':
        damage_index = i
        continue
    elif i % 2 == 0:
        total += int(isbn[i])
    else:
        total += 3 * int(isbn[i])
        
for i in range(10):
    if damage_index % 2 != 0:
        m = total + 3 * i
    else:
        m = total + i
    
    if m % 10 == 0:
        print(i)
        break
        