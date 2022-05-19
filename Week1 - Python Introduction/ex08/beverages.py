class HotBeverage:
	def __init__(self, name="hot beverage", price=0.30, desc="Just some hot water in a cup") -> None:
		self.name = name
		self.price = price
		self.desc = desc

	def description(self):
		return self.desc

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.desc}\n"

a = HotBeverage("coffe", 0.40, "A coffee, to stay awake.")
b = HotBeverage("tea", 0.30)
c = HotBeverage("chocolate", 0.50, "Chocolate, sweet chocolate...")
d = HotBeverage("cappuccino", 0.45, "Un po' di Italia nella sua tazza!")
print(a)
print(b)
print(c)
print(d)