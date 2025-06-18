#find the factorial of first n numbers
num=int(input("enter a number:"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)