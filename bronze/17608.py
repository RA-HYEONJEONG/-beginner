from collections import deque
import sys

N = int(sys.stdin.readline())
arr = deque()
result = deque()

for i in range(N):
    arr.append(int(sys.stdin.readline()))
for i in range(N):
    if i == 0:
        result.append(arr.pop())
        result.append(arr.pop())
    elif i == (N-1):
        None
    else:
        result.append(arr.pop())
    if result[-1] <= result[-2]:
        result.pop()

print(len(result))