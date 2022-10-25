line = "abc def ghijk  lmonp r s tuwxyz GvR"
help(sorted)
wyrazy = line.split()
sorted(wyrazy, key=None, reverse=False)
['GvR', 'abc', 'def', 'ghijk', 'lmonp', 'r', 's', 'tuwxyz']
sorted(wyrazy, key=len, reverse=False)
['r', 's', 'abc', 'def', 'GvR', 'ghijk', 'lmonp', 'tuwxyz']
