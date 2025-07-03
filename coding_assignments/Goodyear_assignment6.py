# Base class
class Animal:
   def __init__(self, name, age, owner_name):
      self.name = name
      self.age = age
      self.owner_name = owner_name

   
   def eat(self):
      print(f"{self.name} is eating.")

   
   def sleep(self):
      print(f"{self.name} is sleeping.")

   
   def make_sound(self):
      print(f"{self.name} makes a generic animal sound.")

 

# Derived class: Dog
class Dog(Animal):
   def __init__(self,name,age,owner_name,breed):
      super().__init__(name,age,owner_name)
      self.breed = breed # unique to dog

   # change sound to bark
   def make_sound(self):
      print(f"{self.name} barks.")

   # unique walk method
   def walk(self):
      print(f"{self.name} is going for a walk.")

 

# Derived class: Cat
class Cat(Animal):
   def __init__(self,name,age,owner_name,color):
      super().__init__(name,age,owner_name)
      self.color = color # unique to cat

   # change sound to meow
   def make_sound(self):
      print(f"{self.name} meows.")

   # unique climb tree method
   def climb_tree(self):
      print(f"{self.name} is climbing a tree.")


# Derived class: Bird
class Bird(Animal):
   def __init__(self,name,age,owner_name,species):
      super().__init__(name,age,owner_name)
      self.species = species # unique to bird

   # change sound to chirp
   def make_sound(self):
      print(f"{self.name} chirps.")

   # unique fly method
   def fly(self):
      print(f"{self.name} is flying in the sky.")



# Test Environment
if __name__ == "__main__":
   dog = Dog(name="Buddy",age=1,owner_name="Sarah",breed="Golden Retriever")
   cat = Cat(name="Whiskers",age=7,owner_name="Chloe",color="Orange")
   bird = Bird(name="Tweety",age=3,owner_name="Bryan",species="Oriole")

   # dog behaviors
   dog.eat()
   dog.sleep()
   dog.make_sound()
   dog.walk()

   # cat behaviors
   cat.eat()
   cat.sleep()
   cat.make_sound()
   cat.climb_tree()

   # bird behaviors
   bird.eat()
   bird.sleep()
   bird.make_sound()
   bird.fly()

