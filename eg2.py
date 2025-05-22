print("kushal \nghimire")
#string operation
str1="kushal"
str2="ghimire"
print(str1+str2)
print(len(str1))
fina=str1+" "+str2
print(fina)
print(len(fina))
print(fina[3])#indexing
print(fina[0:len(fina)])#slicing-->str[starting index:ending index]
print(fina[:4])#str[0:4]

#string function
str="i am a backend developer."
print(str.endswith("er."))
print(str.capitalize())#capitalize 1st character
print(str.replace("e","a"))#str(old,new)
print(str.find("c"))#returing first index of first occurance
print(str.count("am"))
