2.12

line = "abc def ghijk lmonp r s tuwxyz"
words = line.split()
print(words)
['abc', 'def', 'ghijk', 'lmonp', 'r', 's', 'tuwxyz']
letterss = [word[0] for word in words]
nowy = "".join(letterss)
print(nowy)
adglrst
symbols = [word[-1] for word in words]
print(symbols)
['c', 'f', 'k', 'p', 'r', 's', 'z']
nowy1 = "".join(symbols)
print(nowy1)
cfkprsz
