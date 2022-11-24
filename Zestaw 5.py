Zestaw 5

5.2

def simplify(frac):
    a, b = frac
    gcd = euklides(a, b)
    return [a // gcd, b // gcd]

def add frac(frac1, frac2):
    a1, a2 = frac1
    b1, b2 = frac2
    return simplify([a1 * b2 + b1 * a2, a2 * b2])

def sub frac(frac1, frac2):
    a1, a2 = frac1
    b1, b2 = frac2
    return [a1 * b2 - b1 * a2, a2 * b2]

def mul frac(frac1, frac2):
    a1, a2 = frac1
    b1, b2 = frac2
    return [a1 * b2, a2 * b2]

def is posotive(frac):
    return frac[0] * frac [1] > 0

def div frac(frac1, frac2):
    if is zero(frac2):
        raise ZeroDivisionError
    a1, a2 = frac1
    b1, b2 = frac2
    return [a1 * b2, a2 * b1]

def frac2 float(frac):
    return float(frac[0]) / float(frac[1])

def cmp frac(frac1, frac2):
    frac = sub frac(frac1, frac2)
    if is zero(frac):
        retirn 0
    elif is positive(frac):
        return 1
    else:
        return -1

def  test cmp frac(self):
    self.assertTrue(is positive([5,6]))
    self.assertFalse(is positive([-5,6]))
    self.assertTrue(is zero([0, 6]))
    self.assertTrue(is zero(self.zero))
    self.assertFalse(is zero([5, 6]))
    self.assertEqual(cmp frac([1, 2], [1, 3]), 1)
    self.assertEqual(cmp frac ([1, 2],  [1, 2]), 0)
    self.assertEqual(cmp fraac([1, 6, [1, 3]), -1)
