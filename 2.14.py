line = "abc def ghijk lmonp r s tuwxyz"
longest =  max(line.split(), key=len)
print("longest word is: ",  longest)
longest word is:  tuwxyz
line.split()
['abc', 'def', 'ghijk', 'lmonp', 'r', 's', 'tuwxyz']
len(longest)
6
