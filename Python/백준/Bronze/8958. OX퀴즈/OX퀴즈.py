t = int(input())

for _ in range(t):
    ox = input()
    score = []
    if ox[0] == "O":
        score.append(1)
    else:
        score.append(0)
    for i in range(1, len(ox)):
        if ox[i] == "O":
            score.append(score[i-1]+1)
        else:
            score.append(0)
            
    print(sum(score))