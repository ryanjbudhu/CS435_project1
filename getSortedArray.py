def getSortedArray(n):
	arr = []
	for i in reversed(range(1,n+1)):
		arr.append(i)
	return arr
		
print(getSortedArray(10))