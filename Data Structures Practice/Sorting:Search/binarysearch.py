def binarySearch(arr,x):

	if len(arr) == 1 or len(arr) == 0:
		return x in arr
	else:
		mid = arr[len(arr)//2]
		if x == mid:
			return True
		if x < mid:
			return binarySearch(arr[:len(arr)//2],x)
		if x > mid:
			return binarySearch(arr[len(arr)//2:],x)

for i in range(0,11): print(i, binarySearch([1,3,5,7,9,11],i))
