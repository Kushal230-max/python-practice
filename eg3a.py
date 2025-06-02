#tuples->built in datatype that lets us create immutable/(not changeable) sequence of value
tup=(3,2,6,5,3)#tuples can consist also empty data i.e tup=() and for singlee value i.e tup=(1,) otherwise it will print int as datatype
print(type(tup))
print(tup[2])
#slicing
print(tup[0:3])
#tuples method or function
print(tup.index(2))#return index of first occurance
print(tup.count(3))#count total  occurance
fact=(1,)
print(type(fact))