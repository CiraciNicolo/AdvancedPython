from autoinit import *

class Person(metaclass=AutoInit):
  def __init__(self, name, age): pass

class Circle(metaclass=AutoInit):
  def __init__(self, x, y, ray): pass

class Car(metaclass=AutoInit):
  def __init__(self, model, color, plate, year):pass


if __name__ == '__main__':
  a_person = Person('John', 25)
  a_circle = Circle(0, 0, 3.14)
  a_car = Car('Ford Ka', 'Blue', 'AF329SZ', 1999)

  print("A Person of name :- {}, and age :- {}."
      .format(a_person.name,a_person.age))
  print("A Circle centered in <{},{}>, and ray {}."
      .format(a_circle.x,a_circle.y, a_circle.ray))
  print("A {} {} whose plate is {} and was registered in {}."
      .format(a_car.color,a_car.model,a_car.plate,a_car.year))
