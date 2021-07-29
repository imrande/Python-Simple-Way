city = input('Input city name: ').strip().capitalize()
cities = {
    'Hyderabad': 'Aadab',
    'Chennai': 'Vanakkam',
    'Banglore': 'Namaskar'
}

if cities.get(city,'Invalid city name'):
    print(f'Hello, {city}basi, {cities[city]}')