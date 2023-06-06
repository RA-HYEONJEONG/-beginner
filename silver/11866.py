##runtime error version

# import sys
# from collections import deque
#
# N, K = map(int, sys.stdin.readline().split())
#
# num = deque(range(1, N + 1))
# ans = []
#
# while len(num) != 0:
#     for _ in range(K-1):
#         num.append(num.popleft())
#
#     ans.append(str(num.popleft()))
#
#
# print('<' + ',' .join(ans) + '>')



##answer version

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

num = [i for i in range(1, n+1)]
idx = 0
ans = []

while num:
    idx += k-1

    if idx >= len(num):
        idx %= len(num)

    ans.append(str(num.pop(idx)))

print("<", ", ".join(ans), ">", sep="")

