#write the recursive function to print the all the element in a list
fruit=["apple","banana","mango","orange"]
def display(list,idx):
    if(idx==len(list)):
        return
    print(list[idx],end=" ")
    display(list,idx+1)
display(fruit,0)