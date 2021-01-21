
from collections import namedtuple

randomnumber = 100

# create a tuple
t = 12,100,23
# print(t)
# print(t[0])

#  nested tuple
u = t, (500,5000)
# print(u)


# use a tuple to store coordinates and then store them in a set:
coords = namedtuple("Coords", ['x', 'y'])
mycoord = coords(100, 500)
mycoord1 = coords(900, 500)
# print(mycoord.x, mycoord.y)

# create a set and add coords:
myset = set();
myset.add(mycoord);
myset.add(mycoord1);

# print(myset);
# print(type(myset))

# checks the datatype
if isinstance(myset, tuple) :
	print(True)

while True:
	try:
		print("Input integers forever");
		number = int(input("Please enter a number"))
		break
	except ValueError:
		print("No, thats not a number")