num = int(input())
ans_list = []

for i in range(num):
    ans_list.append(list(input()))

score_list = []

for i in ans_list:
    initial_score, total_score = 1,0
    for j in range(len(i)):
        if j == 0:
            if i[j] =='O':
                total_score = 1
            elif i[j] =='X':
                total_score = 0
        elif j > 0:
            if i[j] =='O':
                if i[j-1] == 'O':
                    initial_score += 1
                    total_score += initial_score
                elif i[j-1] == 'X':
                    total_score += 1
            elif i[j] == 'X':
                initial_score = 1
    score_list.append(total_score)


for i in score_list:
    print(i)
