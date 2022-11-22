Zestaw 5

5.2

def simplify(frac):
    a, b = frac
    gcd = euklides(a, b)
    return [a // gcd, b // gcd]
