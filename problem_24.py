class Animal:
    def speak(self):
        print("Animal makes sound")

class dog(Animal):

    def speak(self):
        print("Dog barks")

d = dog()
d.speak()