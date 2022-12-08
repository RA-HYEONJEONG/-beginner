time = list(map(int,input().split()))


H = time[0]
M = time[1]

if H == 0 and M < 45:
    H = 23
    M = M+15

elif H != 0 and M < 45:
    H = H-1
    M = M + 15

else:
    H = H
    M = M-45

print("%d %d" %(H,M))