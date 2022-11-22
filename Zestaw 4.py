Zestaw 4

4.3

def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result


print(factorial(5))

4.4

def fibonacci(n):
    if n < 2:
        return n
    n1, n0 = 0, 1
    for i in range(1, n):
        n1, n0 = n0, n1 + n0
    return n0


print(fibonacci(10))

4.5

def odwracanie(L, left, right):
    left += len(L) if left < 0 else 0
    right += len(L) if right < 0 else 0
    while left < right:
        L[left], L[right] = L[right], L[left]
        left = left+1
        right = right-1


4.6

def sum_seq1(sequence1):
    result = 0
    for item in sequence1:
        if isinstance(item, (list, tuple)):
            result += item
    return result

4.7

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
def flatten(seq):
    alist = []
    for item in seq:
        if isinstance(item, (list, tuple)):
            alist.extend(flatten(item))
        else:
            alist.append(item)
    return alist

print(flatten(seq))
