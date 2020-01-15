# Pytest

Install the Pytest unit testing module with this command:
```bash
pip3 install unittest
```
To use Pytest, create a file in the same directory as the file you want to
test.  You can either use the prefix "test_" or the suffix "\_test".  For
example, if your filename is hello.py, you can use one of these:
- test_hello.py
- hello_test.py

In your test file, put something like this:
```python3
import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure value errors are raised
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
```
This assumes you have a function circle_area in a file called circles.py.

To see documentation on TestCase methods, use:
```python
help(unittest.TestCase.assertSetEqual)
```

To run the tests, use a command like this:
```bash
python3 -m unittest test_circles.py
```
