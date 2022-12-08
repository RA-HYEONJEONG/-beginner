A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))
#print(result)
count = [0,0,0,0,0,0,0,0,0,0]

for i in result:
    for j in range(10):
        if int(i) == j:
            count[j] += 1

#print(count)

for i in count:
    print(i)