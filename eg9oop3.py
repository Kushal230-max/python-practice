#multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("car is starting...")
    @staticmethod
    def stop():
        print("car is stoping...")
class Toyotacar(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(Toyotacar):
    def __init__(self,type,brand):
        self.type=type
        super().__init__(brand)  #super() method
        super().stop()
car1=Fortuner("disel","fortuner")
print(car1.start())
print(car1.brand)


#multiple inheritance
class A:
    var1="welcome to A"
class B:
    var2="welcome to B"
class C(A,B):
    var3="welcome to C"
c1=C()
print(c1.var2,c1.var1)