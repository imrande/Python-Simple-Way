# Abstract class with at least one abstract method can't be instantiated...

# CASE-1
class Test:
	pass
# t = Test() -> OKay

# CASE-2
from abs import ABC, abstractmethod
class Test(ABC):
	pass
# t = Test() -> OKay

# CASE-3
from abs import ABC, abstractmethod
class Test(ABC):
	@abstractmethod
	def m1(self): pass

# t = Test() -> Error

# CASE-4
from abs import ABC, abstractmethod
class Test():
	@abstractmethod
	def m1(self): pass

# t = Test() -> Okay