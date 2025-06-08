#break used to terminate the loop when encountered
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of the loop")
#continue used to terminate the current iteration and continues execution of the loop with the next iteration
n=10
while n>=6:
    if(n==7):
        n-=1
        continue#skip
    print(n)
    n-=1
print("end of the loop")
