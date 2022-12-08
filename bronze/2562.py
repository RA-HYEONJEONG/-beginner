number=[]

for i in range(9):
    number.append(int(input()))

#print(number)

max = 0
for i in number:
    if max < i:
        max = i

print(max)
print(number.index(max)+1)