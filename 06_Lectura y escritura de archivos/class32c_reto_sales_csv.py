import csv, json

monthly_sales = {}

with open("class32c_reto_monthly_sales.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row["Month"]
        sales = int(row["Sales"])
        monthly_sales[month] = sales

print(monthly_sales)
print(type(monthly_sales))

# Convert dictionary to JSON string (ojo, es un string especial)
monthly_sales_json = json.dumps(monthly_sales, indent=4)
print(monthly_sales_json)
print(type(monthly_sales_json))
