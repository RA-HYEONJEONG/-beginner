N = int(input())
man = []
for i in range(N):
    plus = list(map(int, input().split(" ")))
    man.append(plus)
ans = []
for i in range(N):
    count = 0
    for j in range(N):
        if man[i][0] < man[j][0] and man[i][1] < man[j][1]:
            count +=1
    ans.append(count+1)

print(" ".join(map(str,ans)))