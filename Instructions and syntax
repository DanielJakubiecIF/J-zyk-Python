#3.1

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;   # you can't execute more than one statement at a time


for i in "axby": if ord(i) < 100: print (i)  #zła kolejność "if" i "print"

for i in "axby": print (ord(i) if ord(i) < 100 else i) #poprawne

#3.2

L = [3, 5, 4] ; L = L.sort() #przypisanie dwóch różnych komend do jednej wielkości "L"

x, y = 1, 2, 3 #ilość zmiennych nie zgadza się z ilością przypisywanych wartości

X = 1, 2, 3 ; X[1] = 4 #krotki są niezmienne, nie można zmieniać wartości wewnątrz krotki

X = [1, 2, 3] ; X[3] = 4  #próba uzyskania dostepu do elementu który jest poza listą

X = "abc" ; X.append("d") # "append" nie można używać na stringu

L = list(map(pow, range(8))) #brakujący argument dla afunkcji "pow()"


#3.3

max_n = 30
n = 1
while n <= max_n:
    if (n % 3) != 0:
        print(n)
    n = n + 1

#3.4

while True:
    reply = input(float)
    if reply == "stop":
        break
    try:
        number = float(reply)
    except ValueError:
        print("To nie jest liczba!")
    else:
        print(number)
        print(number ** 3)

#3.5

x = 12; row = []
row.extend("|...." for i in range(x))
row.append("|\n0")
row.extend(str(i+1).rjust(5) for i in range(x))
row.append("\n")
print("".join(row))

#3.6

x = 4; y = 2
r1 = "---".join("+" * (x+1)) + "\n"
r2 = "   ".join("|" * (x+1)) + "\n"
print(r2.join([r1] * (y+1)))

#3.8

#a
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if a_set & b_set:
        print(a_set & b_set)
    else:
        print("No common elements")
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

#b

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9]
print(union(lst1, lst2))

#3.9

S = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
Y = list(sum(x) for x in S)
print(Y)

#3.10

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




