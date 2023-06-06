
N = int(input())

mydict = {}

for i in range(N):
    s = input()
    length = len(s)

    if length not in mydict:
        mydict[length] = []

    if s not in mydict[length]:
        mydict[length].append(s)

mydict = {k: mydict[k] for k in sorted(mydict)}

for i in mydict.keys():
    printlist = mydict[i]
    printlist.sort()
    for j in printlist:
        print(j)

