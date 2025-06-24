# f=open("eg7write.txt","w")#overwrite the entire line
# f.write("my name is kushal ghimire.")
f=open("eg7write.txt","a")#add to the file
# f.write("i wanna learn javasrcipt")
f.write("\nThen wanna learn reactjs")
f.close()

#(r+) -> read + overwrite (pointer staring point)- no trumcate
#(w+) -> read + overwrite (no pointer)-trumcate(mean-similar to delete all data of file)
#(a+) -> read + append (pointer end point)- no trumcate

# f=open("eg7write.txt","r+")   ->this is kushal
# f.write("abc")
# print(f.read())               ->abcs is kushal
# f.close()