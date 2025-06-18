#waf to find the fact of n( num as parameter)
def fact(a):
    fac=1
    i=1
    while i<=a:
        fac=fac*i
        i+=1
    print(fac)
fact(6)