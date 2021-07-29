# Mini oop projects

class Movie:
	"""docstring for movie class"""
	def __init__(self, title, hero, heroine, release_year):
		self.title = title
		self.hero = hero
		self.heroine = heroine
		self.release_year = release_year

	def Info(self):
		return (f'Movie name is {self.title}\n'
		f'Movie hero is {self.hero}\n'
		f'Movie heroine is {self.heroine}\n'
		f'Movie release year {self.release_year}')

list_of_movies = []
while True:
	title = input('Movie name is ')
	hero = input('Movie hero name is ')
	heroine = input('Movie heroine name is ')
	release_year = input('Movie release year is ')
	m = Movie(title, hero, heroine, release_year)
	list_of_movies.append(m)
	print('Movie has been added')

	option = input('Do you wanna add more movie [yes/no] ')
	if option.lower() == 'yes':
		continue
	else:
		break

for movie in list_of_movies:
	print(movie.Info())