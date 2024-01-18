pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'tuna',
}
pets.append(pet)

pet = {
    'animal type': 'parakeet',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 1,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")