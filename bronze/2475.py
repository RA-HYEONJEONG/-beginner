orgin = list(map(int,input().split()))

print(orgin)
sum = 0
for i in orgin:
    sum += i*i

critic = sum % 10

print(critic)