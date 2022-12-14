number = int(input())
result = 0

for i in range(1,number+1):
    N = i + sum(map(int,str(i)))

    if N == number:
        result = i
        break

print(result)