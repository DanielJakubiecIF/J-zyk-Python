#Create a function find_axis(v1, v2) which returns the unit
#vector v3, where v3 is perpendicular to the vectors v1 and v2.
#If the vectors v1 and v2 are parallel (or zero) then the
#function should raise an exception (ValueError)

def find_axis(v1, v2):
    v3 = v1.cross(v2)
    if v3 == Vector(0, 0, 0):
        raise ValueError("v1 and v2 are parallel")
    d = v3.length()
    v3 = v3 * (1.0 / d)
    return v3

print(find_axis(Vector(2, 0, 0), Vector(0, 2, 0)))
find_axis(v, v)

#Create the following infinite iterators:
#(a) returning 0, 1, 0, 1, 0, 1, ...,
#(b) returning randomly 0 or 1 on demand,
#(c) returning 0, 1, 0, -1, 0, 1, 0, -1, ...

import itertools
import random

def iter_random(sequence):
    while True:
        yield random.choice(sequence)

it72a = itertools.cycle([0, 1])

it72b = iter_random([0, 1])

it72c = itertools.cycle((0, 1, 0, -1))
