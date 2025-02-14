class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит мяу"


class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит гав"

dog = Dog("вув")
cat = Cat("пеп")

print(dog.speak())
print(cat.speak()) 