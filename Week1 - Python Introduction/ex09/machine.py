
import beverages
import random

class CoffeeMachine:
	def __init__(self):
		self.used = 0

	class EmptyCup(beverages.HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
			self.desc = "An empty cup?! Gimme my money back!"

	def BrokenMachineException(self):
		raise Exception("\033[0;31mThis coffee machine has to be repaired.\033[0m")

	def repair(self):
		self.used = 0

	def serve(self, drink):
		if self.used == 10:
			self.BrokenMachineException()
		self.used += 1
		if (random.randint(2,3) % 2) == 0:
			return self.EmptyCup()
		else:
			return drink

if __name__ == "__main__":
	a = beverages.HotBeverage()
	b = beverages.Coffee()
	c = beverages.Tea()
	d = beverages.Chocolate()
	e = beverages.Cappuccino()
	coffee_machine = CoffeeMachine()
	i = [a, b, c, d, e] * 4
	for _ in i:
		try:
			print("\033[0;32mYou got:\033[0m\n{}".format(coffee_machine.serve(_)))
		except Exception as ex:
			print(ex)
			coffee_machine.repair()
			print("\033[0;32mThe machine has been repaired.\033[0m\n")
