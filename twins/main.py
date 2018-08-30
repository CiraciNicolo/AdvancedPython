from twins import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:
    def __init__(self, cv):
        self.cv = cv
    def add_exam(self, name, mark):
        self.cv[name] = mark
    def average(self):
        return sum(self.cv.values())/len(self.cv)

class Worker:
    def __init__(self, salary):
        self.daily = salary
    def deduction(self, percentage):
        return self.daily*percentage/100
    def salary(self,percentage):
        return (self.daily-self.deduction(percentage))*365

class WorkingStudent(metaclass=Twins([Person,Student,Worker])): pass

if __name__ == '__main__':
    w = WorkingStudent('Walter', 25, dict({'PA':28, 'LP':30}), 100)
    print("The working student {} is {} years old".format(w.name,w.age))
    w.add_exam('TSP', 30)
    print("His current curriculum is:")
    for exam, mark in w.cv.items():
        print(" · {:3} :- {}".format(exam, mark))
    print("... and his current average is {:.2f}".format(w.average()))
    print("Last but not least. He is currently earning {}€".format(w.salary(10)))
