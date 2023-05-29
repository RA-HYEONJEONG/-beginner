def factorial1(n):
    cnt = 1
    for i in range(1,n+1):
        cnt *= i
    return cnt

def factorial2(a,b):
    cnt = 1
    for i in range(a,b+1):
        cnt *= i
    return cnt

N, K = map(int,input().split())

A = factorial2(N-K+1,N)
B = factorial1(K)

print(int(A/B))