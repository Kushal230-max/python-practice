#wap to find the sum of first n number(using while)
num=int(input("enter a number:"))
i=1
sum=0
while i<=num:
    sum=i+sum
    i+=1
print(sum)