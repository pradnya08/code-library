
def largestSum(arr, n):
	
	result = -2147483648

	for i in range(n):
	
		curr_sum = arr[i]
		while (i + 1 < n and
			arr[i + 1] > arr[i]):
		
			curr_sum += arr[i + 1]
			i += 1
		
		if (curr_sum > result):
			result = curr_sum
	
	return result

arr = [1, 1, 4, 7, 3, 6]
n = len(arr)
print("Largest sum = ", largestSum(arr, n))

