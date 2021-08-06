
class Animal:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def jump(self):
        print(f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Cat(Animal):

    def meow(self):
        print(f"{self.name} is meowing")


if __name__ == "__main__":
    dog = Dog(height=100, weight=100, name="MAX", age=19)
    cat = Cat(height=70, weight=80, name="Anna", age=5)
    print(dog.age)
    print(dog.name)
    print(dog.height)
    print(dog.weight)
    dog.jump()
    dog.set_name("Kasha")
    print(dog.age)
    print(dog.name)
    print("/////")
    print(cat.age)
    print(cat.name)
    print(cat.height)
    print(cat.weight)
