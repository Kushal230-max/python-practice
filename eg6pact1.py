#waf to print the lenght of list(list as parameter)
cities=["ktm",'bkt','pkh','ctw']
heroes=['ironman','krish','saktiman']
def list_len(a):
    print(len(a))
list_len(cities)
list_len(heroes)
#print the element of list in single line
def fun(a):
    for el in a:
        print(el,end=" ")
fun(cities)