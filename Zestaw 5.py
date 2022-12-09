import math

def simplify(frac):
    a, b = frac
    gcd = math.gcd(a, b)
    return [a // gcd, b // gcd]

def is_zero(frac):
    return frac[0] == 0

def add_frac(frac1, frac2):
    a1, a2 = frac1
    b1, b2 = frac2
    return simplify([a1 * b2 + b1 * a2, a2 * b2])

def sub_frac(frac1, frac2):
    a1, a2 = frac1
    b1, b2 = frac2
    return [a1 * b2 - b1 * a2, a2 * b2]

def mul_frac(frac1, frac2):
    a1, a2 = frac1
    b1, b2 = frac2
    return [a1 * b1, a2 * b2]

def is_positive(frac):
    return frac[0] * frac [1] > 0

def div_frac(frac1, frac2):
    if is_zero(frac2):
        raise ZeroDivisionError
    a1, a2 = frac1
    b1, b2 = frac2
    return [a1 * b2, a2 * b1]

def frac2_float(frac):
    return float(frac[0]) / float(frac[1])

def cmp_frac(frac1, frac2):
    frac = sub_frac(frac1, frac2)
    if is_zero(frac):
        return 0
    elif is_positive(frac):
        return 1
    else:
        return -1

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): pass

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def  test_cmp_frac(self):
        self.assertTrue(is_positive([5,6]))
        self.assertFalse(is_positive([-5,6]))
        self.assertTrue(is_zero([0, 6]))
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero([5, 6]))
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac ([1, 2],  [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 6], [1, 3]), -1)


    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

