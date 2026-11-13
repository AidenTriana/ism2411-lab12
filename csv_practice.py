import csv
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent
SALE_FILE = DATA_DIR / 'sale.csv'
CLEANED_FILE = DATA_DIR / 'cleaned.csv'
LOG_FILE = DATA_DIR / 'run_log.txt'

print("---ex1---")
with open(SALE_FILE, 'r') as f:
    print(f'opened {SALE_FILE}.')

print("---ex2---")

with open(SALE_FILE, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


print("---ex3---")
with open(SALE_FILE, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f'header: {header}')
    for row in reader:
        print(row)

print("---ex4---")
total_revenue = 0.0
with open(SALE_FILE, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        total_revenue += total

print(f'{product}: {quantity} units at ${price:.2f} each, total: ${total:.2f}')

print("---ex5---")

high_value = []
row_read = 0
with open(SALE_FILE, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        row_read += 1
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        if price > 100:
            high_value.append([product, f"{price:.2f}", quantity_str, f"{total:.2f}"])

with open(CLEANED_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product', 'price', 'quantity', 'total'])
    for row in high_value:
        writer.writerow(row)

print(f"wrote {len(high_value)} of {row_read} rows to {CLEANED_FILE}.")




print("---ex6---")

dict_total = 0.0
with open(SALE_FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        price = float(row['price'])
        quantity = int(row['quantity'])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units at ${price:.2f} each, total: ${total:.2f}")

print(f"total revenue: ${dict_total:.2f}")

print("---ex7---")

summary = {}
with open(SALE_FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row['product']
        total = float(row['price']) * int(row['quantity'])
        summary[product] = summary.get(product, 0) + total

for product in summary:
    print(f"{product}: ${summary[product]:.2f}")

print("---ex8---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, 'a') as f:  
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, 'r') as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"log entries so far: {entries}")

#reflect1
#completing a full etl pipline with csv files, reading, cleaning, and logging the results in excel vs python is interesting since python allows for more automation and flexibility in data processing. In Excel, you would typically have to manually perform each step, which can be time-consuming and prone to errors, especially with large datasets. Python, on the other hand, allows you to write scripts that can handle repetitive tasks efficiently, making it easier to clean and analyze data programmatically. Additionally, Python's libraries provide powerful tools for data manipulation and visualization that go beyond what Excel can offer.

#reflect2
# a real buisness example of using an append mode log file would be in a retail environment where daily sales data is collected. Each day, the sales data could be processed to calculate total revenue, and this information could be appended to a log file. Over time, this log file would serve as a historical record of sales performance, allowing the business to track trends, identify peak sales periods, and make informed decisions based on past performance. This approach ensures that all relevant data is preserved without overwriting previous entries, providing a comprehensive view of the business's financial health over time.