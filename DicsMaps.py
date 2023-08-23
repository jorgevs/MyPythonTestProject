# Dictionaries/Maps =================================================================
super_heroes = {1: 'Spiderman', 2: 'Batman', 3: 'Robin', 4: 'Superman'}

print(super_heroes[1])
del super_heroes[2]
super_heroes[1] = 'Batman'
print("%r" % super_heroes)
print("=============================================================================")
print(len(super_heroes))
print(super_heroes.get(4))
print(super_heroes.keys())
print(super_heroes.values())
print("=============================================================================")
if super_heroes.__contains__('Batman'):
    print("Contains Batman")
elif super_heroes.__contains__('Robin'):
    print("Contains Robin")
else:
    print("Does not contain Batman nor Robin")
print("=============================================================================")
numbered_words = dict()
numbered_words[2] = 'world'
numbered_words[1] = 'Hello'
numbered_words[3] = '!'
print("numbered_words: %r" % numbered_words)

print("=============================================================================")
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

for city, name in cities.items():
    print("The abbreviation %s stands for: %s" % (city, name))
    print(cities[city])
    print(cities.get(city))

# NOTE: If you need to order a dictionary, take a look at the collections.OrderedDict data structure in Python

