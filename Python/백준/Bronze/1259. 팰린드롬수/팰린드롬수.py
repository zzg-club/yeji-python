while True:
    case = input()
    if case == "0":
        break
    
    l = len(case)
    palindrome = True
    for i in range(l//2):
        if case[i] != case[l-i-1]:
            palindrome = False
            
    if palindrome:
        print("yes")
    else:
        print("no")