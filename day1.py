// sort 이용
num = int(input())
num_list = []

for i in range(num):
		n = int(input())
		num_list.append(n)

num_list.sort()

for i in range(num):
		print(num_list[i])


// bubble sort
num = int(input())
num_list = []

for i in range(num):
		n = int(input())
		num_list.append(n)

for i in range(num - 1):
		for j in range(num - i - 1):
				if num_list[j] > num_list[j + 1]:
						num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

for i in range(num):
		print(num_list[i])
