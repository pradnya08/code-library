
import math

def findMean(arr, l, r):
	
	sum, count = 0, 0
	
	for i in range(l, r + 1):
		sum += arr[i]
		count += 1

	mean = math.floor(sum / count)

	return mean

arr = [ 1, 2, 3, 4, 5 ]
	
print(findMean(arr, 0, 2))
print(findMean(arr, 1, 3))
print(findMean(arr, 0, 4))

