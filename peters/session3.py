import os
class change_dir(object):
	def __init__(self,dir_new):
		self.dir_new = dir_new

	def __enter__(self):	
		self.dir_old = os.getcwd()
		os.chdir(self.dir_new)

	def __exit__(self):
		os.chdir(self.dir_old)

class CourseRepo(object):
	def __init__(self, name):
                self.surname = name
	
	@property
	def surname(self):
		return self._surname

	@surname.setter
	def surname(self,name):
		self._surname=name
		self.required = (".git","setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py",self.surname + "/__init__.py",self.surname + "/session3.py") 

	def check(self):
		for entry in self.required:
			if os.path.exists(entry) == False:
				return False
		return True
		
