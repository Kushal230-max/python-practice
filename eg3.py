#list ->can store different type of data type
marks=[67.5,68.5,98.5,78.5]
print(marks)
print(type(marks))
print(marks[2],marks[0])
print(len(marks))
#list->change/mutable but string is not
Student=["kushal",78.5,"bachelor"]
print(Student)
Student[0]="ghimire"
print(Student)
#list slicing
print(marks[0:4])#ending index is not included
#list method
list=[2,5,8,7]
list.append(9)#add a element at the end
print(list)
list.sort()#arrange in ascending order
print(list)
list.sort(reverse=True)#arrange in desending order
print(list)
list.reverse()#reverse the list
print(list)
list.insert(2,0)#inser(index,element)
print(list)
list.pop(2)#removing element at index
print(list)