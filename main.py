from jackscript import *  

# coords = namedtuple("Coords", ['x', 'y'])
# mycoord1 = coords(100, 500)
# mycoord2 = coords(5000, 9000)
# print(coords)

#  checks if one set is the superset of the other
# def isSuperSet():
# myset =set()
# myset.add(mycoord1)
# myset.add(mycoord2)
normalset1 = {2, 3, 4}
normalset2 = {5, 6}

cartesian1 = createCartesian(normalset1, normalset2);
# print(isSubset(normalset1, normalset2));

# cartesian2 = createCartesian( {2}, {100} );

# print(type(cartesian1))
# isRelation(cartesian2, cartesian1)

# create a set of coords:
newset = set([coords(1,1), coords(1,2)])
newset2 = set([coords(1,1), coords(1,1)])

# print(isRelation(newset2, newset))

newset2.clear();
# print(newset2)

# print(isSubset(normalset1, normalset2));
# print(isSuperset(normalset1, normalset2));

# print(Dom(cartesian1))
# print(Range(cartesian1))

print(isBinaryRelation({coords(2,23)}, cartesian1));