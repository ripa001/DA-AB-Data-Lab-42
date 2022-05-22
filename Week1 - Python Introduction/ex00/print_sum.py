import sys

def isfloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

if __name__ == "__main__":
	tot = 0;
	if (len(sys.argv) != 3):
		exit("Wrong arguments")
	a = [x for x in sys.argv[1:] if x.isdigit() or isfloat(x)]
	if len(a) != len(sys.argv[1:]):
		exit("Wrong arguments")
	for x in a:
		tot += float(x)
	print(tot)

