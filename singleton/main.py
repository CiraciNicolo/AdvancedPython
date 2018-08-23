from singleton import *

class A(metaclass=Singleton):
	def __init__(self):
		self.a=1

class B(metaclass=Singleton):
	def __init__(self):
		self.b=1

if __name__ == "__main__":
    a=A()
    a1=A()
    print("a is a1", a is a1)
    a.a=12
    a2=A()
    print("a.a == a2.a == 12", a.a == a2.a == 12)
    b=B()
    print("b is a", b is a)
    b1=B()
    b1.b=42
    print("b is b1", b is b1)
    print("b.b == b1.b == 42", b.b == b1.b == 42)
