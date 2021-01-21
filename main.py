from jackscript import *  

# coords = namedtuple("Coords", ['x', 'y'])
# mycoord1 = coords(100, 500)
# mycoord2 = coords(5000, 9000)
print(coords)

#  checks if one set is the superset of the other
# def isSuperSet():
# myset =set()
# myset.add(mycoord1)
# myset.add(mycoord2)
normalset1 = {2, 5, 6}
normalset2 = {2, 5, 6, 9}

cartesian1 = createCartesian(normalset1, normalset2);
# print(isSubset(normalset1, normalset2));

cartesian2 = createCartesian( {2}, {100} );

# print(type(cartesian1))
isRelation(cartesian2, cartesian1)




