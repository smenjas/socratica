"""
format := (name, radius, density, distance from sun)

Radius: Radius at equator in kilometers
Density: Average density in g/cm^3
Distance from Sun: Avg. distance to sun in AUs

1 Astronomical Unit (AU) is the average distance from the Earth to the Sun
"""

# The planets sorted by distance from the Sun, ascending.
planets = [
    ('Mercury', 2440, 5.43, 0.395),
    ('Venus', 6052, 5.24, 0.723),
    ('Earth', 6378, 5.52, 1.000),
    ('Mars', 3396, 3.93, 1.530),
    ('Jupiter', 71492, 1.33, 5.210),
    ('Saturn', 60268, 0.69, 9.551),
    ('Uranus', 25559, 1.27, 19.213),
    ('Neptune', 24764, 1.64, 30.070)
    ]

# Let's sort by the planets' radii, largest first (descending).
#
# Create a function that returns the 2nd value in the tuple, the radius.
# The input is a tuple of planet data, and the output is the 2nd value,
# which is the equatorial radius. Remember, indices begin at zero.
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
#print(planets) # Jupiter, Saturn, Uranus, Neptune, Earth, Venus, Mars, Mercury

# Now let's find the least dense planet.
size = lambda planet: planet[2]
planets.sort(key=size, reverse=False)
#print(planets) # Saturn, Uranus, Jupiter, Neptune, Mars, Venus, Mercury, Earth

# list.sort() changes the list
# Q: Can you create a sorted copy?
# Q: How do you sort a tuple?
# A: Use sorted()
help(sorted)

