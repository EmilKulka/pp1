def bubbleSort(array):
	n = len(array)
 
	swapped = False

	for i in range(n-1):
		for j in range(0, n-i-1):
			if array[j] > array[j + 1]:
				swapped = True
				array[j], array[j + 1] = array[j + 1], array[j]
		if not swapped:
			return


# Driver code to test above
array = [64, 34, 25, 12, 22, 11, 90]


print("Sorted array is:")
for i in range(len(array)):
	print("% d" % array[i], end=" ")
