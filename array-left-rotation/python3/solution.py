import sys

def rotLeft(a, d):
	return a[d:] + a[0:d] 

if __name__ == '__main__':
	lines = [i.strip() for i in sys.stdin.readlines()]
	n,d = [int(i) for i in lines[0].split()]
	a = [int(i) for i in lines[1].split()]
	
	d = d % n

	result = [str(i) for i in rotLeft(a, d)]

	print(' '.join(result))
