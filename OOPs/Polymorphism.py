
# Example 1: Same method name, different behavior

# class Dog:
#     def speak(self):
#         return "Woof!"
    
# class Cat:
#     def speak(self):
#         return "Meow!"
    
# def animal_sound(animal):
#     print(animal.speak())
    

# dog = Dog()
# cat = Cat()

# animal_sound(dog)
# animal_sound(cat)



#  Example 2: Polymorphism with inheritance

class Animal:
    def speak(self):
        return "some sound"

class Cow(Animal):
    def speak(self):
        return "Moo"

class Sheep(Animal):
    def speak(self):
        return "Baa"
    

for animal in (Cow(), Sheep(), Animal()):
    print(animal.speak())