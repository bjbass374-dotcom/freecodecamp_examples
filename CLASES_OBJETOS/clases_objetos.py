"""DEFINICION DE CLASE DOG Y CREACION DE DOS OBJETOS dogs) A PARTIR DE LA CLASE
USO DE LOS METROS DE LA CLASE CREADA"""

class Dog:
     def __init__(self, name, age):
          self.name = name
          self.age = age

     def bark(self):
          print(f"{self.name.upper()} says woof woof! I'm {self.age} years old...WHAAAAT...?!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

#Call the attributes of dog_1
print(dog_1.name) #attribute name of dog_1
print(dog_1.age)#attribute age of dog_1

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

class Car:
     def __init__(self, color, model):
          self.color = color  # Instance attribute
          self.model = model  # Instance attribute

     def describe(self):
          return f"This car is a {self.color} {self.model}"

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.describe()) # This car is a red Toyota Corolla
print(car_2.describe()) # This car is a green Lamborghini Revuelto


#practice with classes Whorkshop
class MusicalInstrument:
     def __init__(self, name, instrument_type):
          self.name = name
          self.instrument_type = instrument_type

     def play(self):
          print(f'The {self.name} is fun to play!')

     def get_fact(self):
          return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play()
print(instrument_2.get_fact())

#LABORATORIO REALIZADO EN CURSO 
class Planet:
     def __init__(self, name, planet_type, star):
          if not (isinstance(name,str) and isinstance(planet_type,str) and isinstance(star,str)):
               raise TypeError('name, planet type, and star must be strings')
          if not (name and planet_type and star):
               raise ValueError('name, planet_type, and star must be non-empty strings')
          self.name=name
          self.planet_type=planet_type
          self.star=star

     def orbit(self):
          return f'{self.name} is orbiting around {self.star}...'

     def __str__(self):
          return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'    

planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Proxima b", "Terrestrial", "Proxima Centauri")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())