num = input()
num_list = list(num)
num_list.reverse()
num2 = ''.join(num_list)

#print(num2)

number = list(map(int,num2.split()))

print(max(number))