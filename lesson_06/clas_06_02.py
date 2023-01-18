import csv

with open("lesson_06.data.csv", "r") as file:
    reader = csv.reader(file)
    dictionary = {
        row[0]: row[1]
        for row in reader
    }
