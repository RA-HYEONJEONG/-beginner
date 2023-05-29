A, B, V = map(int, input().split())

h = V - A
if A>=V:
    print(1)
else:
    if h % (A-B) == 0:
        cnt = 1 + h // (A-B)
    else:
        cnt = 2 + h // (A-B)

    print(cnt)
