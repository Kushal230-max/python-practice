#from a file containing numbers seperated  by comma print the count if even number
def check():

    with open("eg7practice4.txt","r") as f:
        data=f.read()
        num=data.split(",")
        print(num)
        count=0
        for val in num:
            if(int(val)%2==0):
                count+=1
    print(count)
check()
        