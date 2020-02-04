#define a class
class Vehicle:#(object):
    speed = 0

     #def __new__(cls):
     #    return object.__new__(cls)
    
    def __init__(self, speed = 2): #wartość domyślna prędkości pojazdu
        self.speed = speed

    def IncreaseSpeed(self, increaseAmount):#funkcja speed1
       self.speed += increaseAmount

    def __add__(self, otherVehicle): #?Overloading operators
        return Vehicle(self.speed + otherVehicle.speed)

    def __del__(self):#zwróci komunikat przy usunięciu obiektu
        print("Object has been destroyed")

class Car(Vehicle):#definiowanie klasy 'Car' z dziedziczeniem funkcji z klasy 'Vehicle'
    weight = 1000

    def IncreaseWeight(self, weight): #nowa funkcja tylko dla obiektów z klasy 'Car'
        self.weight += weight

    def IncreaseSpeed(self, increaseAmount):#funkcja speed2, przy dziedziczeniu funkcji, jeżeli w podklasie zdefiniujemy tę samą funkcję w inny sposób, nadpisuje ona funkcję nadklasy w tym konkretnym obiekcie klasy
        self.speed *= increaseAmount
        
#add objects to class
car1 = Vehicle() #wygeneruje wartość domyślną
car2 = Vehicle(345) #zmienia wartość domyślną na danym pojeździe
car3 = Vehicle(0)
car4 = Car(20)
car5 = car1+car2

#access attributes
print(car4.weight)
car4.IncreaseWeight(100)
print(car4.weight)
car4.IncreaseSpeed(5)
print(car4.speed)

print("Speed of car 1: %i" % car1.speed)
print("Speed of car 2: %i" % car2.speed)
print("Speed of car 3: %i" % car3.speed)

car1.IncreaseSpeed(5)
car2.IncreaseSpeed(-100)

print("Speed of car 1: %i" % car1.speed)
print("Speed of car 2: %i" % car2.speed)
#print("Speed of car 3: %i" % car3.speed)
car5.IncreaseSpeed(7)
print("Speed of car 5: %i" % car5.speed)

del car3
