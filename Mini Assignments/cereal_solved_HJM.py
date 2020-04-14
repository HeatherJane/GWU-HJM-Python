import os
import csv
import string

csvreader = '../Resources/cereal.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvreader, 'r') as text:
    reader = csv.reader(text)
    next(reader, None)
    for row in reader:
        if float(row[7]) >= 5:
            cereal = row[0]
            fiber = row[7]
            print(cereal + " has " + fiber + " grams of fiber.")
          
   

