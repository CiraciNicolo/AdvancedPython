from magic import *

@magic(Empty)
class Person:
	def __init__(self, name, gross, netp):
		self.gross_salary = gross
		self.netpercentage = netp
		self.name = name
	def who(self): return self.name
	def salary(self): return self.gross_salary*self.netpercentage/12

@magic(Empty)
class Exam:
	def __init__(self, title, n, ne):
		self.title = title
		self.students = n
		self.exams = ne
	def todo(self):
		return "still {} students should pass the {} exam".format(self.students-self.exams, self.title)

if __name__ == "__main__":
	m = Empty()
	x = Exam("PA", 100, 15)
	y = Exam("TSP", 50, 45)
	p = Person("Bob", 100000, .6)

	try:
		print("m salary :- ",m.salary())
	except Exception as e: print("*** {0}: {1}".format(type(e).__name__, e))
	print("p salary :- ", p.salary())
	print("m salary :- ", m.salary())
	try:
		print("m todo :- ", m.todo())
	except Exception as e: print("*** {0}: {1}".format(type(e).__name__, e))
	print("x todo :- ", x.todo())
	print("m todo :- ", m.todo())
	p.netpercentage=.45
	print("m salary :- ", m.salary())
	print("y todo :- ", y.todo())
	print("m todo :- ", m.todo())
	print("m students :- ",m.students)
	print("x todo :- ", x.todo())
	print("m students :- ",m.students)
	try:
		print("m who :- ",m.who)
	except Exception as e: print("*** {0}: {1}".format(type(e).__name__, e))
