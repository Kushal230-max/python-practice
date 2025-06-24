#private
#atributes
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #this __ helps to protect the data or atributes
    def reset(self):
        print(self.__acc_pass)
A1=Account("73828","fuckingbitch")
print(A1.acc_no)
A1.reset()
#method
class Person:
    __name="kushal"
    def __hello(self):
        print("hi,", self.__name)
    def welcome(self):
        self.__hello()
P1=Person()
P1.welcome()