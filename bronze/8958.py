num = int(input())

for i in range(num+1):
    ans = list(input())
    score,plus = 0,0

    for j in range(len(ans)):
        if j == 0 and ans[j] == 'X':
            score = 0
        elif j == 0 and ans[j] == 'O':
            score = 1
        elif j != 0 and ans[j] == 'O':
            for k in range(j):
                if ans[k] == 'O':
                    plus += 1
            score += plus
    print(score)