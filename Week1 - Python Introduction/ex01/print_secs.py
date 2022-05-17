import sys

if __name__ == "__main__":
	tot = 0;
	if len(sys.argv) != 4:
		exit("Wrong arguments")
	for x in (x for x in sys.argv[1:] if not x.isdigit()):
		exit("Wrong arguments")
	for x in (x for x in sys.argv[1:-1] if x.isdigit()):
		tot = (tot + int(x)) * 60
	tot += int(sys.argv[-1])
	print(tot)

