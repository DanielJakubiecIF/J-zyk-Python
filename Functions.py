#Functions

#4.1
#Let p=(x,y) be a point in a plane. Define the following functions using lambda:
#(a) a test if p is in unit (filled) circle,
#(b) a test if the coordinates of p are positive,
#(c) a sorting key (y decreasing, x increasing),
#(d) a sorting key (the sum |x|+|y|).

lam_unit = lambda p: pow(p[0], 2) + pow(p[1], 2) < 1
lam_pos = lambda p: (p[0] > 0) and (p[1] > 0)


L = [(1,2), (3,-4), (0, 0.5)]
for p in L:
    print(p, lam_unit(p), lam_pos(p))

L.sort(key=lambda p: (-p[1], p[0]))
print(L, "y decreasing, x increasing" )

L.sort(key=lambda p: abs(p[0]) + abs(p[1]))
print(L, "sum |x| + |y|")

#4.2
#Reversing a part of a list in place, reverse_range(L, left, right), the right
#index is included. Write iterative and recursive versions.

def reverse_rangeI(L, left, right):
    while left<right:
        x = L[left]
        L[left] = L[right]
        L[right] = x
        left = left+1
        right = right-1

def reverse_rangeR(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_rangeR(L, left+1, right-1)


L = list(range(10))
reverse_rangeI(L, 2, 8)
print(L)
reverse_rangeR(L, 3, 6)
print(L)

#4.3
#Create the following infinite generators:
#(a) iter_even(), producing even numbers (0, 2, 4, ...),
#(b) iter_odd(), producing odd numbers (1, 3, 5, ...),
#(c) iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...).

def iter_even():
    i = 0
    while True:
        yield i 
        i = i + 2

def iter_odd():
    i = 1
    while True:
        yield i
        i = i + 2

def iter_power(k):
    i = 1
    while True:
        yield i
        i = 1 * k
