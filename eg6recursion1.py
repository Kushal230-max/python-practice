#recursion->when the function calls itself repeatedly
#print n 1 backward
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
    print("end")#call stack->function over function
show(7)