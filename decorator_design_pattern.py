'''
Decorator Design Pattern is used when we want to add behavior to the objects at runtime. The idea behind the decorator pattern
is that we can behavior at runtime by wrapping the object in a decorator class. This helps us in a way that we don't need to
change class structure or inheritance with ever changing requirements.
Example: 
Let's say we have a pizza shop where we have a base pizza and then we can add toppings to that pizza like olives, cheese etc.
Now we can have ever evolving toppings for the pizza in a way that toppings might change, old toppings might be discountinued
or new toppings are added. This will bloat the pizza class. In order to solve this problem we have decorator design pattern.
'''
from abc import ABC, abstractmethod

class Pizza:
    @abstractmethod
    def getCost(self):
        pass

    @abstractmethod
    def addToppings(self):
        pass
    
    @abstractmethod
    def getToppings(self):
        pass


class ThinCrust(Pizza):
    #def __init__(self):
    #    self.pizza = None

    def __init__(self):
         self.pizzaBase = f"Thin Crust"
         self.toppings = []
         self.cost = 5

    def getCost(self):
        return self.cost

    def addToppings(self):
        pass

    def getToppings(self):
        return self.toppings


class CheeseBurst(Pizza):
    #sdef __init__(self):
    #s    self.pizza = None

    def __init__(self):
        self.pizzaBase =  f"Cheese Burst"
        self.toppings = []
        self.cost = 10

    def getCost(self):
        return self.cost

    def addToppings(self):
        pass


#abstract class for toppings
class Toppings(Pizza):
    def __init__(self, pizzaObj):
        self._pizza = pizzaObj

    def getCost(self):
        return self._pizza.getCost()

    def addToppings(self):
        return self._pizza.toppings

    def getToppings(self):
        return self._pizza.toppings


class ExtraCheese(Toppings):
    def addToppings(self):
        self._pizza.toppings.append["Extra Cheese"]

    def getCost(self):
        return self._pizza.getCost()+5


class ExtraOnion(Toppings):
    def addToppings(self, pizza):
        self._pizza.toppings.append["Extra Onion"]

    def getCost(self):
        return self._pizza.getCost()+5


tcPizza = ThinCrust()
cbPizza = CheeseBurst()
print(f"cost of Thin Crust Pizza {tcPizza.getCost()}, cost of Cheese Burst Pizza {cbPizza.getCost()}")
print("Add toppings")
tcPizza = ExtraCheese(tcPizza)
tcPizza = ExtraOnion(tcPizza)
print(f"cost of Thin Crust Pizza, with extra cheese and onion is {tcPizza.getCost()}")
cbPizza = ExtraCheese(cbPizza)
cbPizza = ExtraOnion(cbPizza)
print(f"cost of Cheese Burst Pizza, with extra cheese and onion is {cbPizza.getCost()}")





