import sys


N = int(sys.stdin.readline())

result = dict()

for _ in range(N):
    number = int(sys.stdin.readline())
    if number in result:
        result[number] += 1
    else:
        result[number] = 1

sorted_dict = sorted(result.items())
for k, v in sorted_dict:
    for vv in range(v):
        print(k)

