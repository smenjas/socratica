# Alkaline Earth metals
earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metals.sort() # This sorts the list in place, without creating a copy.
#print(earth_metals)
earth_metals.sort(reverse=True)

# Tuples are immutable, so they don't have a sort attribute.
earth_metals = ('Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium')
#earth_metals.sort() # This raises an AttributeError.

# list.sort() changes the list
# Q: Can you create a sorted copy?
# Q: How do you sort a tuple?
# A: Use sorted()
#help(sorted)

earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
sorted_earth_metals = sorted(earth_metals) # This copies the list
#print(sorted_earth_metals) # The copy is sorted
#print(earth_metals) # The original is untouched

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
sorted_data = sorted(data) # Copy the tuple into a sorted list
#print(type(sorted_data))

print(sorted(set('Alphabetical'.lower())))
