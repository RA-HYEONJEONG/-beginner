from collections import OrderedDict

N = int(input())
mydict = OrderedDict()
for i in range(N):
    n,s = input().split(" ")
    if int(n) not in mydict:
        mydict[int(n)] = []
    mydict[int(n)].append(s)

mydict = OrderedDict((k, mydict[k]) for k in sorted(mydict))

for k,v in mydict.items():
    for name in v:
        print(k,name)
