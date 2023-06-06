N = int(input())
mydict = {}

for i in range(N):
    x,y = map(int,input().split())

    if x not in mydict:
        mydict[x] = []
    mydict[x].append(y)

sortedkey = sorted(mydict.keys())
for i in sortedkey:
    values = mydict[i].sort()
    for j in range(len(mydict[i])):
        print(i, mydict[i][j])