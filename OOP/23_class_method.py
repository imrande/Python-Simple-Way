class Bird:
	wings = 2

	@classmethod
	def fly(cls, name):
		print(f'{name} flying with {cls.wings} wings...')

Bird.fly('Eagle')
Bird.fly('Parot')
print()

# =========================
class Test:
	count = 0

	def __init__(self):
		Test.count += 1

	@classmethod
	def get_number_of_objects(cls):
		return cls.count

	def delete_obj(self):
		del self
		Test.count -= 1

t = Test()
t2 = Test()
t3 = Test()
t4 = Test()
t.delete_obj()
t4.delete_obj()
print(Test.get_number_of_objects())