class Car():
    max_speed=200
    def __init__(self,make,model,color,speed=0): #Constructor Method
        self.make=make
        self.model=model
        self.color=color
        self.speed=speed

    def accelerate(self,acceleration): #Method
        if self.speed+acceleration <=Car.max_speed:
            self.speed+=acceleration
        else:
            self.speed=Car.max_speed

    def get_speed(self): #Method
        return self.speed

car1=Car("Dodge","Ford","Blue")
car1.accelerate(30)
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")

car2=Car("Hyundai","Elantra","Blue")
car2.accelerate(20)
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")


a=1

def do(x):
    a=100
    return(x+a)

print(do(1))