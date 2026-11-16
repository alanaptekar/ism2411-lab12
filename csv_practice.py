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

import csv

total_revenue = 0.0

with open("data/sales.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        
        row_total = price * quantity
        total_revenue += row_total
        
        print(f"{product}: {quantity} units x ${price:.2f} = ${row_total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")

import csv

total_rows = 0
written_rows = 0

with open("data/sales.csv", mode="r", newline="") as infile, \
     open("data/cleaned.csv", mode="w", newline="") as outfile:
    
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    
    # Write the required header row
    writer.writerow(["Product", "Price", "Qty", "Total"])
    
    for row in reader:
        total_rows += 1
        
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        row_total = price * qty
        
        if row_total > 100:
            writer.writerow([product, f"{price:.2f}", qty, f"{row_total:.2f}"])
            written_rows += 1

print(f"Wrote {written_rows} qualifying rows out of {total_rows} original rows.")

import csv

total_revenue = 0.0
total_quantity = 0

with open("data/sales.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total_revenue += price * quantity
        total_quantity += quantity

print(f"Total Quantity: {total_quantity}")
print(f"Total Revenue: ${total_revenue:.2f}")