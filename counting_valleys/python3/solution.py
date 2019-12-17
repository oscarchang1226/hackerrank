import sys

def countingValleys(n, s):
	current = 0
	valleys = 0
	for i in range(n):
		j = 1 if s[i] == 'U' else -1
		if current == 0 and j == -1:
			valleys += 1
		current += j
	return valleys 

if __name__ == '__main__':
	
	lines = [i.strip() for i in sys.stdin]
	n = int(lines[0])
	s = lines[1]
	
	result = countingValleys(n, s)

	print(result)
	
