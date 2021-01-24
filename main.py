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
normalset1 = {2, 3, 4, 8}
normalset2 = {2, 3, 4}
normalset3 = {2, 3, 4, 5}

cartesian1 = createCartesian(normalset1, normalset2);
cartesian2 = createCartesian(normalset1, normalset3);
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
# print(isBinaryRelation({coords(2,23)}, cartesian1));

# print(isRelation(cartesian2, cartesian1));
# print(isIrreflexive(cartesian2, normalset1));


# testing symmetry....
myset = { coords(2,3), coords(3,2), coords(8,3), coords(3,8)}
print(isSymmetric(myset,normalset1  ))