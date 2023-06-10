planet = {
    'name': 'Earth',
    'moons': 1,
    'oceans': 7
}

print(planet.get('name'))
print(planet['name'])


# GET VALUE OF wibble
wibble = planet.get('wibble')  # Returns None
# wibble = planet['wibble']  # Throws KeyError


# UPDATE VALUE OF name
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# UPDATE KEYS IN DICTIONARY
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
# SAME
planet['name'] = 'Jupiter'
planet['moons'] = 79


# ADD NEW KEY 'orbital period'
planet['orbital period'] = 4333
print(planet)


# TO REMOVE ONE KEY
planet.pop('orbital period')


# DICTIONARIES IN DICTIONARIES (JS SAME)
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)


# GET ALL KEYS
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


# CHECKS IF KEY EXISTS
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1


total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'There was {total_rainfall}cm in the last quarter.')


people = [
    {"name": "saul", "age": 25},
    {"name": "deisy", "age": 26},
    {"name": "joselyn", "age": 10},
]

# WAYS TO ITERATE AN ARRAY OF DICTIONARIES
for person in people:
    for values in person.values():
        print(values)


for person in people:
    name, age = person.values()
    print(name)
    print(age)

for person in people:
    for key in person.keys():
        print(f"{key}: {person[key]}")
