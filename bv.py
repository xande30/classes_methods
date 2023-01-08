
from colorama import Fore, Back

class Person:
	def __init__(self,name,age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay *= (1.0 + percent)
	def __str__(self):
		return ('<%s =>> %s: %s, %s>' %(self.__class__.__name__,self.name, self.job, self.pay))

class Manager(Person):
	def __init__(self, name, age,pay):
		Person.__init__(self, name, age, pay, 'manager')
	def giveRaise(self, percent, bonus=0.1):
		Person.giveRaise(self,percent + bonus)


if __name__ == '__main__':
	mike = Person('Mike Dully',43)
	jenny = Person('Jenny Smithsson earns: ', 45, 50000,'cmputer programmer')
	steve = Person(name='Steve Liamson earns: ',age=39,pay=56000)
	print(Fore.CYAN,jenny.pay,jenny.lastName())
	for obj in (mike,jenny,steve):
		obj.giveRaise(.10)
		print(Fore.MAGENTA,obj)
