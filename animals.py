class Animal:
    def move(self):
        pass
    def make_sound(self):
        pass

class Bird(Animal):
    def move (self):
        print("Flying")

    def make_sound(self):
        print("chirp")

class Cat(Animal):
    def move(self):
        print("walk") 
    def make_sound(self):
        print("meow")

class Fish(Animal):
    def move(self):
        print("swimming")
    def make_sound(self):
        print("Bop")                               