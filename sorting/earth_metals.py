# Alkaline Earth metals
earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)

# Tuples are immutable, so they don't have a sort attribute.
earth_metals = ('Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium')
#earth_metals.sort() # This raises an AttributeError.
