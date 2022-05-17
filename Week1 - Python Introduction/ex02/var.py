if __name__ == "__main__":
	list = ["quarante-deux", 42.0, True, [42], {42 : 42}, (42,), set()]
	for el in list:
		print(f"\033[0;32m{el}\033[0m has a type \033[91;91m{type(el)}\033[0m")