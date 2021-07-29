
| Instance Variable      | Class Varible |
| ----------- | ----------- |
| These are object level varaibles      | These are class level variables       |
| For every object a separate copy will be created   | A single copy will be created at class level and shared by all objects of that class        |
| By using one object reference, if we are trying to perform any changes to the instance variables, then those changes won't be reflected to remaining objects.      | If we perform any change to the class variables then those changes will be reflected to all objects...       |

```py
class Test:
	a = 10

	def __init__(self):
		self.b = 20

t1 = Test()
t2 = Test()
Test.a = 888
t1.b = 999

print(f't1: {t1.a} {t1.b}') # => 888 999
print(f't2: {t2.a} {t2.b}') # => 888 20
```
