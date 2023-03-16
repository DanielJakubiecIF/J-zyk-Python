2.10
#Nie licz ilości wyrazów, licz ilość whitespace ""

line = "abc def ghijk lmonp r s tuwxyz"

ilość = (line.count(" ") + 1)
print(ilość)
7
line = "abc   def ghijk    lmonp    r s tuwxyz"
print(ilość)
7

2.11

line = "word"

colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)
print(result)
redbluegreenyellow
słowo = ["w", "o", "r", "d"]
result = "_".join(słowo)
print(result)
w_o_r_d

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

2.13

line = "abc def ghijk lmonp r s tuwxyz"
len(line)
30
x = line.count(" ")
print(x)
6
wyrazy = len(line)
długość = wyrazy -  x
print(długość)
24

2.14

line = "abc def ghijk lmonp r s tuwxyz"
longest =  max(line.split(), key=len)
print("longest word is: ",  longest)
longest word is:  tuwxyz
line.split()
['abc', 'def', 'ghijk', 'lmonp', 'r', 's', 'tuwxyz']
len(longest)
6

2.15

L = ["1", "2", "3", "4", "5", "6", "7"]
napis =  "".join(L)
print(napis)
1234567

2.16

line = "abc def ghijk  lmonp r s tuwxyz GvR"
print(line.replace("GvR", "Guido van Rossum"))
abc def ghijk  lmonp r s tuwxyz Guido van Rossum

2.17

line = "abc def ghijk  lmonp r s tuwxyz GvR"
help(sorted)
wyrazy = line.split()
sorted(wyrazy, key=None, reverse=False)
['GvR', 'abc', 'def', 'ghijk', 'lmonp', 'r', 's', 'tuwxyz']
sorted(wyrazy, key=len, reverse=False)
['r', 's', 'abc', 'def', 'GvR', 'ghijk', 'lmonp', 'tuwxyz']

2.18

liczba = "100000000000000000"
x = liczba.count("0")
print(x)
17

2.19

L = [1, 2 , 3 , 45, 67, 78, 987,654,321]
[str(item).zfill(3) for item in L]
['001', '002', '003', '045', '067', '078', '987', '654', '321']


