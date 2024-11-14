'''
Singleton design pattern is used when you want only one instance of a class present throughout the lifecycle of a program
and each time an object is created it should return reference to that instance.
Useful in the situations where you want only one entry point to your class
'''

class SingletonClass:
    instance = None
    name = None
    def __new__(cls, name):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.name = name
            return cls.instance
        else:
            return cls.instance
    
    #def __init__(self, name):
    #    self.name = name

    @staticmethod
    def getInstance(self):
        return self.instance

    def getName(self):
        print(self.name)

    def setName(self, name):
        self.name = name


obj1 = SingletonClass("ABC")
print("id obj1 ", id(obj1))
obj1.getName()
obj1.setName("BCD")
obj2 = SingletonClass("DEF")
print("id obj2 ", id(obj1))
obj2.setName("XYZ")
obj2.getName()



