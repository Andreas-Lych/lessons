import csv

with open("dictionary.csv", "r") as file:
    reader = csv.reader(file)
    dictionary = {
        row[0]: row[1]
        for row in reader
    }