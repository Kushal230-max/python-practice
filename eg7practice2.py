#write a function that replace all the occurance of python with java in above file
with open("eg7practice1.txt","r") as f:
    data=f.read()
    print(data)
new_data=data.replace("python","java")
print(new_data)
with open("eg7practice1.txt","w") as f:
    f.write(new_data)