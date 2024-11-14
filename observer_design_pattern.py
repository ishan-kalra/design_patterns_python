'''
observer design pattern is used when one object aka subject or observable needs to notify other objects aka observers about
any change in it's state.
The main uses are in event-driven systems or pub-sub kind of systems when an update has to be sent to all other subcribers dynamically
This promotes loose coupling between the objects.
potential drawbacks are fanout problem when there are too many subscribers or memory leaks when observers are not removed 
properly.
'''

'''
In below example implement amazon shopping cart where a product goes out of stock and we click notify me. So when the product comes back
in stock the subscribers are notified about it.
'''

from abc import ABC, abstractmethod

class Product:
    _observers = []

    def __init__(self, productId, state):
        self.productId = productId
        self.state = state

    def addObserver(self, observerObj):
        self._observers.append(observerObj)

    def removeObserver(self, observerObj):
        self._observers.remove(observerObj)

    def changeState(self, state):
        self.state = state
        for obs in self._observers:
            obs.update(state)


class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class Customer1(Observer):
    def update(self, state):
        print(f"The product is {state}")

class Customer2(Observer):
    def update(self, state):
        print(f"The product is {state}")


p = Product(1, "OUT_OF_STOCK")
c1 = Customer1()
c2 = Customer2()

print("Since product is out of stock observers are added")
p.addObserver(c1)
p.addObserver(c2)

p.changeState("IN_STOCK")
