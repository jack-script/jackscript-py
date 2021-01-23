from collections import namedtuple

coords = namedtuple("Coords", ['x', 'y'])

""" 
I need a function here that is going to confirt the type of params..
Especially one that checks if a <set> is the type of the parameter  
"""


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
	return createCartesian(normalset1,normalset1);

# fucntion that checks if a se4t is a subset of another:
def isSubset(normalset1, normalset2):
	# print(len(normalset2))
	"""I need to make sure that  """
	# if(len(normalset1) > len(normalset2)):
		# return False;
	for i in normalset1:
		if i not in normalset2:
			return False;
	return True

# superset is supposed to be the second parameter
def isSuperset(normalset1, normalset2):
	if isSubset(normalset1, normalset2) != True:
		return False;

	for i in normalset1:
		if i not in normalset2:
			return False;
	return True


#  both params teake in set of coords(or... cartesians) THIS IS IMPORTANT
def isRelation(normalset1, cartesianProduct):
	try: # make sure params are of type set
		if isinstance(normalset1, set) != True or isinstance(cartesianProduct, set) != True:			
			raise Exception('Wrong Type, first and second args must be <set>')
	except Exception as inst:
		print(type(normalset1))
		print(inst.args)
	for i in normalset1:
		if i not in cartesianProduct:
			return False
	return True

# Dom function:
#  this function takes in a cartesian product
def Dom(cartesianProduct):
	newSet = set();
	for i in cartesianProduct:
		newSet.add(i.y);
	return newSet;
	
def Range(cartesianProduct):
	newSet = set();
	for i in cartesianProduct:
		newSet.add(i.x);
	return newSet;




# isBinaryRelation
#  named it R because its a relation from The_Product()
#  R is also a set
""" Basically a binary relation is when a ser->R is a sbuset of the sqrt(A) where A is a normal set """
def isBinaryRelation(R, normalSet):
	cartesianProduct = createCartesian(normalSet, normalSet);
	return isSubset(R, cartesianProduct)


# PROPERTIES OF RELATIONS........

# takes a set of coords and a normal set....
""" We will then take the second param and create a cartesian product for them """
def isReflexive(ReflexiveSet, SuperSet):
	#  first check if the ReflexiveSet is a relation to the cartesian Product...
	try:
		if isRelation(ReflexiveSet, SuperSet) != True:	
			raise Exception('Wrong Type, First param must be relation of param two')
	except Exception as inst:
		print(type(normalset1))
		print(inst.args)
	SuperSetProduct = createCartesian(SuperSet, SuperSet);
	return "success";




def isIrreflexive():
	pass

def isSymmetric():
	pass

def isAntiSymmetric():
	pass

def isTransitive():
	pass

def isTrichotomy():
	pass

def inverseRelation():
	pass

def relationComposition():
	pass
