# ---------- Imports ----------
import csv
from csv import writer

# ------------ Variables ------------ 
rows = []
temp_rows = []

# ------------ Helper Functions ------------
def substring_after(s, delim):
    return s.partition(delim)[2]

def convertStrToList(string):
    newString = string.replace("'", "")
    li = list(newString.split(','))
    return li

# ----------------------------------- Data Formatting -----------------------------------
with open("test_1.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rowString = str(row)
        formattedRowString = substring_after(rowString, ", '1', '',")
        finalString = formattedRowString[:-1]
        print(finalString)
        temp_rows.append(finalString)

with open('table2.csv', 'a') as f_object:
    writer_object = writer(f_object)
    for i in temp_rows:
        a = convertStrToList(i)
        writer_object.writerow(a)
    f_object.close()

