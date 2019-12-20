import sys

def minimumBribes(q):
	# Iterate each element in list except last item
	# for each item check difference of current position and initial position = d
	# if d >= 3 return and print "Too chaotic"
	# add d to accumulator
	# predict next item
	# if next item is not the predicted value (current value - d) add 1 to accumulator
	
	result = 0
	for i in range(len(q) - 1, -1, -1):
		if (q[i] - (i + 1)) > 2:
			result = "Too chaotic"
			break
		for j in range(max(0, q[1]-3), i):
			if q[j] > q[i]:
				result += 1
	print(result) 

if __name__ == "__main__":
	lines = [i.strip() for i in sys.stdin.readlines()]
	t = int(lines[0])
	lines = lines[1:]
	for i in range(t):
		n = lines[0]
		q = [int(i) for i in lines[1].split()]
		lines = lines[2:]
		
		minimumBribes(q)
