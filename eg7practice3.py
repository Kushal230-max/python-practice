# search if the word "using" exist inn the file or not
def check_for_word():
    with open("eg7practice1.txt","r") as f:
        data=f.read()
        if(data.find("using")!=-1):
             print("found")
        else:
            print("not found")
check_for_word()
#waf to find which line of the file does the word "java" occure first Print-1 if word not found
def check_for_line():
    word="java"
    data=True
    line=1
    with open("eg7practice1.txt","r")  as f:
        while data:
            data=f.readline()
            if(word in data):
                print("line:",line)
                return
            line+=1
    return -1
print(check_for_line())