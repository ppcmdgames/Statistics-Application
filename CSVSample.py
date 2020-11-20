# A sample program to read data from .CSV files

import pandas as pd
import time

data = pd.read_csv('population.csv')

# Print all values
print(data)

# Print only the first few values
print("\nEnter the number of initial values to display: ")
# Parse to integer
firstn = int(input())

if isinstance(firstn, int):
    # Display the values from the top
    print(data.head(firstn))
    # Alternative: print(data.head[1:2])
else:
    print("Error! Moving Forward >>")

# Display the names of all columns
print("\nDisplaying the names of all columns.")
print(data.columns)

# Display a specific column
print("\nEnter the name of any column whose values to display (case sensitive): ")
cname = input()
if cname=="Population" or cname=="x location" or cname=="y location":
    # Display all values of that column
    print(data[cname])
else:
    print("\nError! Moving Forward >>>")

# Condition to verify if variable is string: isinstance(variable, type)

# Not working
# Display multiple columns
#print("\nEnter the number of the first column (in the previously mentioned order): ")
#rl1=int(input())
#print("\nEnter the number of the last column (in the previously mentioned order): ")
#rl2=int(input())
print("\nDisplaying the values of column 'x location': \n")
# Display values of x location
print(data['x location'])

# Display a specific row
print("\nEnter the number of any row: ")
rown=int(input())-1
# Display the contents of that row
print(data.iloc[rown])

# Display data from a specific cell
# Syntax: print(data.iloc[rown-1,colmn-1])
print("\nDisplaying data in row 2, column 2: ")
print(data.iloc[1,1])

# Exit the program
print("\n Exiting in 5 s from now...")
# Wait for 5 seconds before exiting
time.sleep(5)
