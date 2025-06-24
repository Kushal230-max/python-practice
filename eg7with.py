with open("eg7with.txt","r") as f:
    data=f.read()
    print(data) #no need of f.close()

with open("eg7with.txt","w") as f:
    f.write("i am a good guy")
    