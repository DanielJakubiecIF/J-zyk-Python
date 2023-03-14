2.1
#Create a long positive integer. Find the number of zeros.

x = 1937574903030

S1 = "1937574903030"

S2 = "0"

ilość = (S1.count(S2))

print(ilość)

2.2
#Explain the results.

x = 5                         # assigning value 5 to x
x == 5 and 3                  # 3; 'True and Anything' returns 'Anything', but not converted to 'bool', 
x == 4 and 3                  # False; 'False and Anything' returns 'False', 'Anything' is not checked, 
3 and x == 5                  # True; one of them is true
3 and x == 4                  # False; none of them is true

isinstance(True, int)         # True; True can be interpreted as value of 1
isinstance(True, bool)        # True; Booleans represent one of two: true or false

2.3
#Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021

L = (range(1, 2023, 2))

suma_listy = 0

for i in L:
    suma_listy += i ** 2

print(suma_listy)

2.4
#(a) Find Unicode code points (int) for all characters of your name

"Daniel" -->  [68, 97, 110, 105, 101, 108]

#Prepare the periodic table (ten elements) as a list
#pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].
#Use pt to print a table (3 right + 20 left + 6 center + 10 right)

pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (2,"Helium","He",4), (2,"Helium","He",4), (2,"Helium","He",4), (2,"Helium","He",4), (2,"Helium","He",4),(2,"Helium","He",4), (2,"Helium","He",4), (2,"Helium","He",4),]

#print(*pt, sep = "\n")


r1 = "+" + "+".join(["---", "--------------------", "------", "----------"]) + "+" + "\n"
r2 = "|" + "|".join(["No.", "Name (en)".ljust(20), "Symbol", "Weight (u)"]) + "|" + "\n"
r3 = "|" + "|".join(["1".rjust(3), "Hydrogen".ljust(20), "H".center(6), "1".rjust(10)]) +"|"+ "\n"


print(r1, r1.join([r2, r3]), r1)

for (a, b, c, d) in pt:
    print("| {} | {} | {} | {} |".format(a, b, c, d))


2.5
#Let S be a long string (many lines). Find the number of black characters in S [not whitespace, see the method S.isspace()].
#Find the number of words in S (a word is a sequence of black characters).
#Find the longest word in S.
#Sort words from S according to (1) the lexicographic order, (2) the length. 

S = "Let S be a long string (many lines). Find the number of black characters in S not whitespace, see the method"

długość = len(S)
białe_znaki = S.count(" ")


ilość_znaków = długość - białe_znaki

longest = max(S.split(), key=len)

wyrazy = S.split()
ilość_wyrazów = len(wyrazy)

lexicographic_order = sorted(wyrazy, key=None, reverse=False)
length_order = sorted(wyrazy, key=len, reverse=False)

print("ilość znaków w stringu:", ilość_znaków)
print("najdłuższy wyraz w stringu:", longest)
print("ilość wyrazów w stringu:", ilość_wyrazów)
print("lexicographic_order:", lexicographic_order)
print("length_order:", length_order)

2.6
#Find and explain the results

t = (2, 4)              #tuple
print(t[2])             #indexing begins with 0 not with 1
t.append(6)             #tuple doesn't have the attribute append
a, b = t ; print(a, b)  #I am no sure here. a and b are assigned to values 2 and 4 in tuple that's why print(a, b) gives 2 and 4
2.7
#Create a dict for conversion of roman numerals/strings (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers. Use different methods.

#1
keys = ["I", "V", "X", "L", "C", "D", "M"]
values = [1, 5, 10, 50, 100, 500, 1000]
D = dict(zip(keys, values))
print(D)

#2
keys = ["I", "V", "X", "L", "C", "D", "M"]
values = [1, 5, 10, 50, 100, 500, 1000]
D = {}

for (k, v) in zip(keys, values):
    D[k] = v
print(D)

