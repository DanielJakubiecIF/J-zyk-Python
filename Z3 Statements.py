Statements

3.1
#For a given word, print it in squares.

word = "Daniel"

n = len(word)

r1 = "---".join("+"*(n+1))
r2 = "| " + (" | ".join(word)) + " |"



print("\n".join((r1, r2, r1)))

3.2
#Make a loop over integer numbers from 1 to 40.
#If x is divided by 5 then print a message 'x is divided by 5'.
#If x is divided by 7 then print a message 'x is divided by 7'.
#If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
#Skip x = 13.
#If x is not divided by 5 and x is not divided by 7 then print a message 'x is not important'.
#Prepare two solutions with 'while' and 'for' loops.

#for
for item in range(1, 41, 1):
    if (item % 5 == 0) and (item % 7 == 0):
        print(item, "is divided by 5 and 7")
    elif item == 13:
        continue
    elif (item % 5 == 0):
        print(item, "is divided by 5")
    elif (item % 7 == 0):
        print(item, "is divided by 7")
    elif (item % 5 !=0) and (item % 7 !=0):
        print(item, " is not important")

#while
item = 0

while (item <= 39):
    item = item + 1
    if (item % 5 == 0) and (item % 7 == 0):
        print(item, "is divided by 5 and 7")
    elif (item % 5 == 0):
        print(item, "is divided by 5")
    elif (item % 7 == 0):
        print(item, "is divided by 7")
    elif (item % 5 !=0) and (item % 7 !=0):
        print(item, " is not important")

3.3

#Create the following variables: n = 2022
#x = math.pi   # save with 5 digits after a dot (import 'math' first!)
#word = "Python"; polish = "książka"   # 'book' in English
#Write the variables to a text file "vars.txt",
#one line for one variable.
#Print the file content on the screen.

import math

n = 2022
x = math.pi
word = "Python"
polish = "książka"

with open("vars.txt", "w") as outfile:
    for item in (n, x, word, polish):
        outfile.write("{}\n".format(item))

print("data saved . . . ")

with open("vars.txt", "r") as infile:
    print(infile.read())
    for line in infile:
        print(line, end=" ")

