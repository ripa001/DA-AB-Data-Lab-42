class HotBeverage:
	def __init__(self, name="hot beverage", price=0.30, desc="Just some hot water in a cup") -> None:
		self.name = name
		self.price = price
		self.desc = desc

	def description(self):
		return self.desc

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}\n"

class Coffee(HotBeverage):
	def __init__(self, name="coffee", price=0.40, desc="A coffee, to stay awake.") -> None:
		super().__init__(name, price, desc)

class Tea(HotBeverage):
	def __init__(self, name="tea", price=0.30) -> None:
		super().__init__(name, price)

class Chocolate(HotBeverage):
	def __init__(self, name="chocolate", price=0.50, desc="Chocolate, sweet chocolate...") -> None:
		super().__init__(name, price, desc)

class Cappuccino(HotBeverage):
	def __init__(self, name="cappuccino", price=0.45, desc="Un po' di Italia nella sua tazza!") -> None:
		super().__init__(name, price, desc)

if __name__ == "__main__":
	a = HotBeverage()
	b = Coffee()
	c = Tea()
	d = Chocolate()
	e = Cappuccino()
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)