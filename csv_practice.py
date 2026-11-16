import csv

with open('data/sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import csv

with open('data/sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    header = next(reader) 
    print("Header:", header) 

    for row in reader:
        print(row)