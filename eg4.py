#dictionary used to store the data value in key:value pair.they are changeable and unorder anddon't allow duplicate key
info={
     "name":"kushal",
     12:"twelve",
     "sub":["java","python"],
     "surname":"kg"
}
print(info)
print(info["name"])
info["surname"]='ghimire'
print(info)
nulldict={}
nulldict["name"]="kushal"
print(nulldict)
#nested dictionary
student={
    "name":"kushal",
    "subject":{
        "chem":89,
        "maths":79,
        "phy":76
    },
     "age":34
}
print(student["subject"]['maths'])
#dictionary method/function
print(student.keys())#return all keys
print(tuple(student.keys()))#in tuple
print(list(student.values()))#return all values
rand=list(student.items())#return all key and values as tuple
print(rand)
print(student.get("name"))#it hepls ti return the value and it also make the program errorfree
#print(student.get("name2"))#it will print none if the key doesn't exist so the program can esaily run beside thie
newdict={"city":"ktm","abc":"sddf"}
student.update(newdict)#helps to all new key and value
print(student)
