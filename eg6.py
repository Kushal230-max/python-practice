#function->block of code that perform a specific task
def calc_sum(a,b):
    sum=a+b
    print(sum)
calc_sum(1,2)
calc_sum(4,6)#decrease redundancy->decrease repeatation of code
def eg(f,g):#parameters
    return f+g
print(eg(2,3))#function call;arguments
#built in functioon such as print(),len(),range(),type()
#defaultparameter->Assigning the default value to parameter,which is used when no argument is passed
def mul(a=2,b=7):
    print(a*b)
mul()