#too map the real world scenarios, we started using object in code.this is called objecct oriented programming


#constructor
class student:
    college_name="CCT"#class attributes
    # default constructor
    def __init__(self):
        pass
    #paramerized constructor
    def __init__(self,fullname,marks,age):
        self.name=fullname#object attributes
        self.marks=marks
        self.age=age
        print("i am constructor")
        print(self)
    def welcome(self):  #method
        print("welcome home",self.name)
    def myage(self):
        return self.age
s1=student("kushal",78,20)
print(s1)
print(s1.name)
print(s1.marks) 
print(s1.college_name)#student.college_name
s1.welcome()
my_age=s1.myage()
print(my_age)