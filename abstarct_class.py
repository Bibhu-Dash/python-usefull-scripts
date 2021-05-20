
from abc import ABC, abstractmethod

class Employee(ABC):
	@abstractmethod
	
	def calculate_salary(self, sal):
		pass


class Developer(Employee):
	def calculate_salary(self, sal):
		final_salary =sal * 1.10   ####increase salary by 10%
		return final_salary


emp1 = Developer()
print(emp1.calculate_salary(10000))