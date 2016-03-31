# Maps/Dictionaries =================================================================
super_heroes = {1: 'Spiderman', 2: 'Batman', 3: 'Robin', 4: 'Superman'}
print(super_heroes[1])
del super_heroes[2]
super_heroes[1] = 'Batman'
print(len(super_heroes))
print(super_heroes.get(4))
print(super_heroes.keys())
print(super_heroes.values())

if super_heroes.__contains__('Batman'):
    print("Contains Batman")
elif super_heroes.__contains__('Robin'):
    print("Contains Robin")
else:
    print("Does not contain Batman nor Robin")


numbered_words = dict()
numbered_words[2] = 'world'
numbered_words[1] = 'Hello'
numbered_words[3] = '!'