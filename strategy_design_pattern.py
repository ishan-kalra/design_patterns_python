'''
What is a strategy design pattern?
It is a design pattern which is when there is a need to select any dynamic algorithm or implementation.
For example when the child classes have their own implementation of something apart from base class and each child
can have same or diff implementation from each other. There is a chance that two more child classes have same implementation 
This adds to code duplicity and if their is some change in the algorithm then the change has to take place at multiple places.

Question: which design principle is violated if we don't have strategy design pattern. 
SOLID 
S = Single Responsibility Principle
O = Open Closed Principle
L = Liskov Substitution Principle
I = Interface abstraction Principle
D = Dependency Inversion Principle
'''
'''
We can implement this design pattern by taking an example of cars
A car can have a base class and child classes can be sports car, family van, etc
Now if we define drive method in base class, then each child class can decide to write their own drive method as need arises.
Hence their is a need to select drive implementation dynamically.
'''

from abc import ABC, abstractmethod

class Car:
    def __init__(self, type):
        self.__type = type

    def drive(self):
        print("This is a normal drive method")

    def getType(self):
        print(self.__type)

    def setType(self, type):
        self.__type = type

class SportsCar(Car):
    def __init__(self, type):
        super().setType(type)
    def drive(self):
        print("I have sports driving method")

class FamilyCar(Car):
    def __init__(self, type):
        super().setType(type)

    def drive(self):
        print("I have safe driving method")

class Sedan(Car):
    def __init__(self, type):
        super().setType(type)

    def drive(self):
        print("I have safe driving method")


sports = SportsCar("sports")
family = FamilyCar("family")
sedan = Sedan("sedan")

sports.getType()
sports.drive()

family.getType()
family.drive()

sedan.getType()
sedan.drive()

'''
The problem in above code is that each child class is having it's own drive metod implementation.
To avoid this probelm we have a driving type interface
'''

class CarsNew(ABC):

    def __init__(self):
        self.__type = None
    
    def getType(self):
        print(self.__type)

    def setType(self, type_):
        self.__type = type_

    @abstractmethod
    def drive(self):
        pass


class SportsDriving(CarsNew):
    def drive(self):
        print("Sports Driving Method")

class FamilyDriving(CarsNew):
    def drive(self):
        print("Family driving method")


class SedanNew(CarsNew):
    __drivingStrategy = None

    def __init__(self, type_, drivingAlgo):
        self.__drivingStrategy = drivingAlgo
        super().__init__()
        super().setType(type_)

    def drive(self):
        self.__drivingStrategy.drive()


class SportsNew(CarsNew):
    __drivingStrategy = None

    def __init__(self, type_, drivingAlgo):
        self.__drivingStrategy = drivingAlgo
        super().__init__()
        super().setType(type_)

    def drive(self):
       self.__drivingStrategy.drive()


class FamilyNew(CarsNew):
    __drivingStrategy = None

    def __init__(self, type_, drivingAlgo):
        self.__drivingStrategy = drivingAlgo
        super().setType(type_)

    def drive(self):
        self.__drivingStrategy.drive()

drivingModeSports = SportsDriving()
drivingModeFamily = FamilyDriving()

sedanNew = SedanNew("sedan", drivingModeSports)
familyNew = FamilyNew("family", drivingModeFamily)
sportsNew = SportsNew("sports", drivingModeSports)


sportsNew.getType()
sportsNew.drive()

familyNew.getType()
familyNew.drive()

sedanNew.getType()
sedanNew.drive()


