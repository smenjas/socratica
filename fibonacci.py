#!/usr/bin/env python3

import logging
from functools import lru_cache

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = 'fibonacci.log',
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("The input must be a positive integer.")
    if n < 1:
        raise ValueError("The input must be a positive integer.")
    if n == float('inf'):
        return float('inf')
    if n in [1, 2]:
        return 1
    if n > 2:
        n = fibonacci(n-1) + fibonacci(n-2)
    return n

for i in range(1, 41):
    x = fibonacci(i+1)
    y = fibonacci(i)
    z = x / y
    print(str(i) + ": " + str(x) + ", " + str(z))
