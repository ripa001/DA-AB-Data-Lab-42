
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
		if (random.randint(0,7) % 7) == 0:
			return self.EmptyCup()
		else:
			return drink

a = beverages.HotBeverage("coffe", 0.40, "A coffee, to stay awake.")
b = beverages.HotBeverage("tea", 0.30)
c = beverages.HotBeverage("chocolate", 0.50, "Chocolate, sweet chocolate...")
d = beverages.HotBeverage("cappuccino", 0.45, "Un po' di Italia nella sua tazza!")
m = CoffeeMachine()
list = [a, b, c, d]

for _ in range(25):
	num = random.randint(0, 3)
	try:
		print("\033[0;32mYou got:\033[0m\n{}".format(m.serve(list[num])))
	except Exception as ex:
		print(ex)
		m.repair()
		print("\033[0;32mThe machine has been repaired.\033[0m")
