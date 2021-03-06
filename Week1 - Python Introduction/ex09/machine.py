
import beverages
import random

class CoffeeMachine:
	def __init__(self):
		self.used = 0

	class EmptyCup(beverages.HotBeverage):
		def __init__(self, name="empty cup", price=0.3, desc="An empty cup?! Gimme my money back!") -> None:
			super().__init__(name, price, desc)

	class BrokenMachineException(Exception):
		def __init__(self, *args: object) -> None:
			super().__init__("\033[0;31mThis coffee machine has to be repaired.\033[0m")

	def repair(self):
		self.used = 0

	def serve(self, drink):
		if self.used == 10:
			raise self.BrokenMachineException()
		self.used += 1
		if (random.randint(2,3) % 2) == 0:
			return self.EmptyCup()
		else:
			return drink()

if __name__ == "__main__":
	coffee_machine = CoffeeMachine()
	i = [beverages.HotBeverage, beverages.Coffee, beverages.Tea, beverages.Chocolate, beverages.Cappuccino] * 4
	for _ in i:
		try:
			print("\033[0;32mYou got:\033[0m\n{}".format(coffee_machine.serve(_)))
		except coffee_machine.BrokenMachineException as ex:
			print(ex)
			coffee_machine.repair()
			print("\033[0;32mThe machine has been repaired.\033[0m\n")
