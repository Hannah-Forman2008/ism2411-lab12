#Reflection questions
#1. Compare to Excel Python is able to automate repetitive tasks
#, calculate totals and overall process large amounts of data.
#While Excel is better for creating chars or viewing information on
# a spreadsheet easier.
#
#2. An append mode log can probably be used by a 
#businuess to record daily sales reports. It is helpful because it can save
#each new entry without deleting previous ones.
print("--Exercise 2--")
import csv
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--Exercise 3--")
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)


print("--Exercise 4--")
import csv
total_revenue = 0
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")


print("--Exercise 5--")
import csv
original_count = 0
written_count = 0
with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])
        for row in reader:
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity
            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1
print(f"Rows written: {written_count} out of {original_count}")


print("--Exercise 6--")
import csv
total_revenue = 0
with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")


print("--Exercise 7--")
import csv
sales_summary = {}
with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total
for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

print("--Exercise 8--")
from datetime import datetime
with open("data/run_log.txt", "a") as file:
    timestamp = datetime.now()
    file.write(f"{timestamp} - Total Revenue: $1869.51\n")
print("Run log updated!")






