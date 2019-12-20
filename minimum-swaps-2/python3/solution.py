import sys

def minimumSwaps(arr):
	target = arr.copy()
	target.sort()
	number_of_swaps = 0
	
	while(arr != target):

		incorrect_indexes = []

		# Get indexes that are incorrect order
		for i in range(incorrect_idx, len(arr)):
			if (arr[i]-1) != i:
				incorrect_indexes.append(i)

		
		# Swap values that are in incorrect indexes
		for i in incorrect_indexes:
			temp = arr[arr[i] - 1]
				arr[arr[i] - 1] = arr[i]
				arr[i] = temp
				number_of_swaps += 1

	return number_of_swaps
		

if __name__ == "__main__":
	lines = sys.stdin.readlines()
	n = int(lines[0])
	arr = [int(i) for i in lines[1].split()]
	
	res = minimumSwaps(arr)

	print(res)
