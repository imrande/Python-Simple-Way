"""
If we are creating child class for abstract class, then for every abstract
method of parent class compulsory we should provide implementation in the child
class, otherwise child class is also abstract and we can't create object for child class...
"""

# CASE-1
from abc import ABC, abstractmethod
class Test(ABC):
	@abstractmethod
	def m1(self): pass

class SubTest(Test):
	pass

# s = SubTest() -> Error

# CASE-2
from abc import ABC, abstractmethod
class Test(ABC):
	@abstractmethod
	def m1(self): pass

	@abstractmethod
	def m2(self): pass

class SubTest(Test):
	def m1(self): print('M1 method')

# sub = SubTest() -> Error

# CASE-3
from abc import ABC, abstractmethod
class Test(ABC):
	@abstractmethod
	def m1(self): pass

	@abstractmethod
	def m2(self): pass

class SubTest(Test):
	def m1(self): print('M1 method')
	def m2(self): print('M2 method')

# sub = SubTest() -> OKay

# CASE-4
from abc import ABC, abstractmethod
class Test(ABC):
	@abstractmethod
	def m1(self): pass

	def m2(self): pass

class SubTest(Test):
	def m1(self): print('M1 method')

# sub = SubTest() -> OKay