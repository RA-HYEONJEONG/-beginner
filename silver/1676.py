def factorial(number):
    res = 1
    for i in range(number):
        res *= (i+1)
    return res

def print_result(n):
    number = str(n)
    for i in range(len(number),0,-1):
        if len(number) == 1:
            print('0')
            break
        if number[i-1] != '0':
            print(str(len(number)-i))
            break




N = int(input())

cal = factorial(N)
result = print_result(cal)
