#search a num x in a tuples using loop
a=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter a number:"))
i=0
while i<len(a):
    if(x==a[i]):
        print("found!!")
        break
    else:
        print("finding...")
    i+=1