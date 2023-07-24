#Modules

#5.1
#For a given directory (top) find the number of bytes taken
#by PDF files in the directory tree (".pdf" extensions).
#The code should be in the function find_pdf_size(top).
#In order to test the current directory we run find_pdf_size(".").

import os

def find_pdf_size(top):
   
    top = r'C:\Users\Predator\Desktop\Materiały naukowe'
    size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.endswith(".pdf"):
                fullpath = os.path.join(root, name)
                print(fullpath)
                size += os.path.getsize(fullpath)
    return size

print("Amount of bytes of PDF files in this directory: {} ".format(find_pdf_size(' . ')))

#5.2
#Create the function print_working_days(date1, date2),
#where 'date1' and 'date2' are strings of the form 'YYYY-MM-DD'.
#The function prints dates of working days (from Monday to Friday)
#in the given range, 'date2' is excluded.

import datetime

def print_working_days(date1, date2):
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)
    delta = datetime.timedelta(days=1)
    day = d1
    while day < d2:
        if day.weekday() < 5:
            print(day.isoformat())
        day = day + delta

print_working_days("2023-01-01", "2023-05-01")

#5.3
#Create the generator random_walk(start) for a 1D random walker.
#If a position at a certain moment is x, then the next position
#can be x+1 or x-1 with equal probabilities. Find the final
#position after 100 moves (start=0). Repeat experiments.

import random

def random_walk(start = 0):
    pos = start
    while True:
        yield pos
        pos += random.choice([-1, 1])

print("random walk 1D(hitting the wall)")
for pos in random_walk():
    print(pos, end=" ")
    if abs(pos) == 5:
        break

print()
print("The possitions  after 100 stpes")
resuls = []
