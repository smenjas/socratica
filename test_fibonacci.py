import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, fibonacci, None)
        self.assertRaises(TypeError, fibonacci, '')
        self.assertRaises(TypeError, fibonacci, ())
        self.assertRaises(TypeError, fibonacci, [])
        self.assertRaises(TypeError, fibonacci, set())
        self.assertRaises(TypeError, fibonacci, {})

    def test_values(self):
        self.assertRaises(ValueError, fibonacci, -1)
        self.assertRaises(ValueError, fibonacci, 0)

    def test_fibonacci(self):
        self.assertAlmostEqual(fibonacci(1), 1)
        self.assertAlmostEqual(fibonacci(2), 1)
        self.assertAlmostEqual(fibonacci(3), 2)
        self.assertAlmostEqual(fibonacci(4), 3)
        self.assertAlmostEqual(fibonacci(5), 5)
        self.assertAlmostEqual(fibonacci(6), 8)
        self.assertAlmostEqual(fibonacci(7), 13)
        self.assertAlmostEqual(fibonacci(8), 21)
        self.assertAlmostEqual(fibonacci(40), 102334155)
        infinity = float('inf')
        self.assertAlmostEqual(fibonacci(infinity), infinity)
