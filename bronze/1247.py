import sys
def find_sign(arr):
    sum = 0
    for i in arr:
        sum += i
    if sum > 0:
        sign = '+'
    elif sum <0:
        sign = '-'
    else:
        sign = '0'
    return sign
for i in range(3):
    N = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(N)]
    sign = find_sign(numbers)
    print(sign)



