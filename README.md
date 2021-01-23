### functions still to build:


0. superset
1. isRealation()
2. domain
3. range
4. codomain
5. 


### Documentation:

##### Installation
install jackscript-py
`pip3 install jackscriptpy`

```python
import * from jackscriptpy
```

##### How to create a set:
sets are created how you would normally create your set in python; as said earlier This library consnist of a set of functions and doesnt make any new data structures.
Therefore all set methods from the python standard library will work like usual
```python 
mySet = set()

```

##### How to create a coordinate(coord):
coordinates are created as so

```python
mycoordinate = coord(1, 2) # this sets x to 1 and y to 2

```

##### advanced...
```python
# add a coordinate to a set, using the coordinate created above:
myset.add(mycoordinate);

# as expected, the standard library methods will work as usual
myset.clear()
print(myset)  # returns set()
```

##### checking whether a set is a subset of another...
```python
set1 = {2, 5, 6}
set2 = {2, 5, 6, 9}
```
Looking at the above code; its clear that set1 should be the subset of set2, we get our answer by calling the function `isSubset()`
```python
answer = isSubset(set1, set2) # returns True 
print(answer) # prints True
```

<h5>Simmilarly we can test if a set is a superset of another</h5>

```python
set1 = {2, 5, 6}
set2 = {2, 5, 6, 9}

answer = isSuperset(set2, set1) # returns True 
print(answer) # prints True
```
<h5>Create a cartesian product</h5>

```python
#create a cartesian product by calling the createCartesian() function
```

<h5>Check if a product is a relation of another</h5>
<p>the function is called: <b>isRelation()</b> </p>

```python 
""" 
	first create a cartesian product from sets:
	there are obviously multiple ways of creating cartesianProducts; we'll use more complicated route to demonstrate the use:
"""
# Create a couple of normal sets
normalset1 = {2, 3, 4} # another way would be: normalset1 = Set([2,3,4])
normalset2 = {2, 3, 4}
normalset3 = {2, 3}

cartesian1 = createCartesian(normalset1, normalset2);
	cartesian2 = createCartesian(normalset1, normalset3); 
```

<p>as u can see above; we used <code>normalset1</code> and <code>normalset3</code> to create a <code>cartesian2</code></p>

<p>so technically, <code>cartesianProduct2</code> should be a relation of <code>cartesian1</code>. We test this theory in the function below, in continuation of the above code.</p>

```python
print(isRelation(cartesian2, cartesian1)); # returns true
```



<!-- write domain and range documentation here -->



<!-- a Binary Relation is a set that is the subset of any Cartesian product 
	if isSubset(R, createCartesian(A, B)) returns true... then R is a BinaryRelation of S
-->





