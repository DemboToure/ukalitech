import json
from .models import SalaryDesignation, Employee

class SalaryBulletin():
	"""docstring for SalaryBulletin"""
	def __init__(self, emp):
		self.emp = vars(emp)
		sds = SalaryDesignation.object.all() 
		self.salaryDesi = [ vars(sd) for sd in sds ]
		