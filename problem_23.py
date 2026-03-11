class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")


p1 = Person("Nic", 25)
p1.introduce()