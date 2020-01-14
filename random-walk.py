import random

def naive_random_walk(n):
    """ Return coordinates after n block random walk. """
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'E', 'S', 'W'])
        if step == 'N':
            y += 1
        elif step == 'E':
            x += 1
        elif step == 'S':
            y -= 1
        elif step == 'W':
            x -= 1
    return (x, y)

def random_walk(n):
    """ Return coordinates after n block random walk. """
    x, y = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(n):
        dx, dy = random.choice(directions)
        x += dx
        y += dy
    return (x, y)

number_of_walks = 10000

for walk_length in range(1, 31):
    no_transport = 0 # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_ratio = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length,
        " / % of no transport = ", 100*no_transport_ratio)
