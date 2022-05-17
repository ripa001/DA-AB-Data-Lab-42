import sys

if __name__ == "__main__":
	tot = 0;
	if (len(sys.argv) != 3):
		exit("Wrong arguments")
	for x in (x for x in sys.argv[1:] if x.isdigit()):
		tot += int(x)
	print(tot)

