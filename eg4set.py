#set is the collection ofthe unordered items.Each element in the set must be unique and immutable 
#cannot store list and dictionary
collection={1,2,2,2,"abc" ,"cdg" ,"abc"}
print(collection)
print(type(collection))
print(len(collection))#ignore the repeated items
#empty set syntax
apple=set() #->if we write apple={},this will be dict
print(type(apple))
#set method
apple.add(1)#add an element
apple.add(3)
apple.add(3)
apple.add((4,5))
apple.add("jysgak")
print(apple)
apple.remove(3)#remove the element
print(apple)
print(apple.pop())#remove random element
apple.clear()#empties the set
print(apple)
#union and intersection
set1={1,2,3}
set2={2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

