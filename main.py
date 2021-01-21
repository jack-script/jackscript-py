from collections import namedtuple

coords = namedtuple("Coords", ['x', 'y'])
mycoord1 = coords(100, 500)
mycoord2 = coords(5000, 9000)


# rules of this set is that you have to pass in 2 normal sets... 
def createCartesian(normalset1, normalset2):
	""" This function takes in 2 sets and returns a set of coords """
	resultSet = set();
	coords = namedtuple("Coords", ['x', 'y'])
	try:
		if isinstance(normalset1, set) != True or isinstance(normalset1, set) != True:
			raise Exception('Wrong Type, Typ must be a set')
	except Exception as inst:
		print(type(normalset1))
		print(inst.args)
	
	# create a set of coordinates
	for i in normalset1:
		for j in normalset2:
			tempCoord = coords(i, j);
			resultSet.add(tempCoord);
	return resultSet

# creates a cartisan product from one set
def setSquare(normalset1):
	createCartesian(normalset1,normalset1);

# fucntion that checks if a se4t is a subset of another:
def isSubset(normalset1, normalset2):
	for i in normalset1:
		if i not in normalset2:
			return False;
	return True




#  checks if one set is the superset of the other
# def isSuperSet():
myset =set()
myset.add(mycoord1)
myset.add(mycoord2)
normalset1 = {2, 5, 6}
normalset2 = {2, 5, 6, 9}

# createCartesian(normalset1, normalset2);
print(isSubset(normalset1, normalset2));