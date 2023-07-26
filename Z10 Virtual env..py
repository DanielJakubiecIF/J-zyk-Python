#10.1
#Create a virtual environment for this course using 'venv' or 'virtualenv'. Install numpy, matplotlib, pandas. Send me a list of commands used (with outputs). 

python -m venv .venv
pip install numpy
Requirement already satisfied: numpy in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (1.24.3)

pip install matplotlib
Requirement already satisfied: matplotlib in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (3.7.1)
Requirement already satisfied: numpy>=1.20 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (1.24.3)
Requirement already satisfied: packaging>=20.0 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (23.1)
Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (1.4.4)
Requirement already satisfied: pillow>=6.2.0 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (10.0.0)
Requirement already satisfied: pyparsing>=2.3.1 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (3.1.0)
Requirement already satisfied: fonttools>=4.22.0 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (4.40.0)
Requirement already satisfied: python-dateutil>=2.7 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (2.8.2)
Requirement already satisfied: cycler>=0.10 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from matplotlib) (0.11.0)
Requirement already satisfied: six>=1.5 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)

pip install pandas
equirement already satisfied: pandas in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (2.0.3)
Requirement already satisfied: numpy>=1.21.0 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from pandas) (1.24.3)
Requirement already satisfied: pytz>=2020.1 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2023.3)
Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2.8.2)
Requirement already satisfied: tzdata>=2022.1 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2023.3)
Requirement already satisfied: six>=1.5 in c:\users\predator\appdata\local\programs\python\python310\lib\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)

#10.2
#Create pd.Series where 'index' contains days of the current month (numpy.datetime64 instances or 
#pandas.DatetimeIndex) and 'data' contains some numbers (temperatures at noon, currency rates, ...). 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days = np.arange("2023-01-01", "2023-05-01", dtype="datetime64[D]")
print("len days{}".format(len(days)))
temperatures = np.random.randint(10, 30, len(days))
t_series = pd.Series(data=temperatures, index = days)
print(t_series)
t_series.plot()
plt.show()

#10.3
#Create pd.DataFrame for the periodic table (ten elements). Column names are 'Name', 'Symbol', 'Weight'. 'index' starts from 1 for hydrogen. 

import pandas as pd 


names = ["Hydrogen", "Hellium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
symbols = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"] 
weights = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20]
numbers = range(1, 11)
periodic_table = pd.DataFrame({"Name": names, "Symbol": symbols, "Weight": weights}, index = numbers)
print(periodic_table)
