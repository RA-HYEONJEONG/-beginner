test_case = int(input())
num = []
for i in range(test_case):
    num.append(list(map(int,input().split())))

result = []
score = 0
for i in num:
    score = i[0]+i[1]
    result.append(score)

for i in result:
    print(i)