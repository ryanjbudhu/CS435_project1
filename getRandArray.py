import random
def getRandArray(n,end=100000):
	arr = []
	while len(arr)<n:
		num = random.randint(0,end)
		if num not in arr:
			arr.append(num)
	return arr

#print(getRandArray(10))