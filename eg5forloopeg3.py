#search for a num x in a give tuple by for loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter a number:"))
idx=0
for val in tup:
    if(x==val):
        print("found at index:",idx)
        break
    idx+=1