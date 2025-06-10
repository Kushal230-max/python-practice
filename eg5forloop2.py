str='my name is kushal'
for val in str:
    if(val=='k'):
        print("found!! o")
        break
    print(val)
else:#else cae is not execute while break
    print("end")