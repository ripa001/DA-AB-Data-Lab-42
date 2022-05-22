import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if (len(sys.argv) != 2):
	exit("Argoument error")
list = [k for k, v in capital_cities.items() if v == sys.argv[1].capitalize()]
if (len(list)):
	print([k for k, v in states.items() if v == list[0]][0])
else:
	print("Unknown capital city")
