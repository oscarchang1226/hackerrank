import sys

def minimumBribes(q):
	# Iterate each element in list except last item
	# for each item check difference of current position and initial position = d
	# if d >= 3 return and print "Too chaotic"
	# add d to accumulator
	# predict next item
	# if next item is not the predicted value (current value - d) add 1 to accumulator
	print(q) 

if __name__ == "__main__":
	lines = [i.strip() for i in sys.stdin.readlines()]
	t = int(lines[0])
	lines = lines[1:]
	for i in range(t):
		n = lines[0]
		q = [int(i) for i in lines[1].split()]
		lines = lines[2:]
		
		minimumBribes(q)
