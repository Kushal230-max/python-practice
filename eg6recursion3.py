#write a recursive function to calculate the sum of n natural number
def calc(n):
    if(n==1):
        return 1
    else:
        return n + calc(n-1)
print(calc(3))