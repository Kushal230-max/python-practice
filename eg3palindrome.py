#check if the list contains palindrome element
list1=[1,2,3,2,1]
list2=[]
list2=list1.copy()
list1.reverse()
if (list1==list2) :
    print("palindrome")
else :
    print("not palindorme")