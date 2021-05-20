
class Student:

	perc_rise = 1.05
	
	def __init__(self,first,last,marks):
		self.first=first
		self.last=last
		self.marks=marks
		self.email=first+'.'+last+'@school.com'
	
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	
	def apply_raise(self):
		self.marks=int(self.marks * self.perc_rise)

class Dumb(Student):
	perc_rise = 1.10
	def __init__(self,first,last,marks,prog_lang):
		super().__init__(first,last,marks)
		self.prog_lang = prog_lang



std1 = Student('Bibhu','Dash',80)
std2 = Student('Pratik','Swain',70)

std3 = Dumb('Arabind','Das',30,'Python')

print(std3.prog_lang)
