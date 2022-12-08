#number, score에 과목수, 점수 각각 입력
#number는 int, score는 list형태
number = int(input())

score = list(map(int, input().split()))

#print(number)
#print(score)

#점수 중에 최고점 찾기
max = 0

for i in score:
    if max<i:
        max =i

#print(max)


#새로운 평균 제작
newscore=[]
for i in score:
    scores = i/(max)*100
    newscore.append(scores)

#print(newscore)

sum = 0

for i in newscore:
    sum += i

average = sum/number
print(average)