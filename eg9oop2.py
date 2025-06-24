#single inheritance
class Car:
    color="Black"
    @staticmethod
    def start():
        print("car is starting...")
    @staticmethod
    def stop():
        print("car is stoping...")
class Toyotacar(Car):
    def __init__(self,name):
        self.name=name
car1=Toyotacar("fortunur")
print(car1.name,car1.color)
print(car1.start())