num = []
while True:
    A,B,C = map(int,input().split())
    if A == 0 and B == 0 and C == 0:
        break
    else:
        num.append(A)
        num.append(B)
        num.append(C)
        num.sort()
        #print(num)
        a, b, c = num[0], num[1], num[2]

        if a*a + b*b != c*c:
            print("wrong")
            num = []
        else:
            print("right")
            num = []


