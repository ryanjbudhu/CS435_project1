import random
def getRandArray(n):
	arr = []
	while len(arr)<n:
		num = random.randint(0,10000)
		if num not in arr:
			arr.append(num)
	return arr

print(getRandArray(10))