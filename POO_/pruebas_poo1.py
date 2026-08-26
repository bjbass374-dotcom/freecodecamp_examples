#example for name mangling, used by noy overwriting on Patern class
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}

#another hand, example without double underscore on atribute of Parent class 
class Parent:
   def __init__(self):
       self.data = 'Parent data'

class Child(Parent):
   def __init__(self):
       super().__init__()
       self.data = 'Child data'

c = Child()
print(c.__dict__)  # {'data': 'Child data'}