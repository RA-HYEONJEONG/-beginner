N = int(input())

for i in range(N):
    R,S = input().split()
    for j in list(S):
        print(j*(int(R)),end = "")
    print()