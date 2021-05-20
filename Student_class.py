
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


std1 = Student('Bibhu','Dash',80)
std2 = Student('Pratik','Swain',70)

print(std1.email)
print(std2.email)

#print(std1.__dict__)
#print(Student.__dict__)

print(std1.marks)
std1.apply_raise()
print(std1.marks)
