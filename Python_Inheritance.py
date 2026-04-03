# Python Inheritance Example

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


# Child Class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(self.name, "says Woof ")


# Another Child Class
class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow ")


# Creating objects
dog1 = Dog("Buddy")
cat1 = Cat("Kitty")

# Calling methods
dog1.speak()
cat1.speak()

# OUTPUT:
# Buddy says Woof 
# Kitty says Meow 
