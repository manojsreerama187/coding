import csv
import random


num_orders = 100  

def generate_random_order(order_id):
    products = ["Widget A", "Widget B", "Widget C", "Widget D"]
    product = random.choice(products)
    quantity = random.randint(1, 20)
    price = round(random.uniform(4.99, 14.99), 2)
    return [order_id, product, quantity, price]


with open("customer_orders.csv", mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    
    csv_writer.writerow(["OrderID", "Product", "Quantity", "Price"])
    
    
    for order_id in range(1, num_orders + 1):
        order_data = generate_random_order(order_id)
        csv_writer.writerow(order_data)

print(f"{num_orders} random orders have been generated and saved to 'customer_orders.csv'.")


def read_customer_orders(filename):
    orders = []
    try:
        with open(filename, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                order = {
                    'OrderID': int(row['OrderID']),
                    'Product': row['Product'],
                    'Quantity': int(row['Quantity']),
                    'Price': float(row['Price'])
                }
                orders.append(order)
        return orders
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []


def total_revenue(orders):
    revenue = sum(order['Quantity'] * order['Price'] for order in orders)
    print(f"Total Revenue: ${revenue:.2f}")


def most_popular_product(orders):
    product_quantity = {}
    for order in orders:
        product = order['Product']
        quantity = order['Quantity']
        product_quantity[product] = product_quantity.get(product, 0) + quantity
    most_popular = max(product_quantity, key=product_quantity.get)
    print(f"Most Popular Product: {most_popular}, Total Quantity Ordered: {product_quantity[most_popular]}")


def average_price(orders):
    average = sum(order['Price'] for order in orders) / len(orders)
    print(f"Average Price: ${average:.2f}")

def top_products_by_revenue(orders, n=5):
    products_revenue = {}
    for order in orders:
        product = order['Product']
        revenue = order['Quantity'] * order['Price']
        products_revenue[product] = products_revenue.get(product, 0) + revenue
    top_products = sorted(products_revenue.items(), key=lambda x: x[1], reverse=True)[:n]
    print("Top 5 Products by Revenue:")
    for product, revenue in top_products:
        print(f"{product}: ${revenue:.2f}")

def write_product_summary(orders, filename):
    product_summary = {}
    for order in orders:
        product = order['Product']
        quantity = order['Quantity']
        revenue = order['Quantity'] * order['Price']
        if product not in product_summary:
            product_summary[product] = {'TotalQuantityOrdered': quantity, 'TotalRevenue': revenue}
        else:
            product_summary[product]['TotalQuantityOrdered'] += quantity
            product_summary[product]['TotalRevenue'] += revenue

    with open(filename, mode="w", newline="") as csv_file:
        fieldnames = ['Product', 'TotalQuantityOrdered', 'TotalRevenue']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for product, summary in product_summary.items():
            csv_writer.writerow({'Product': product, 'TotalQuantityOrdered': summary['TotalQuantityOrdered'], 'TotalRevenue': summary['TotalRevenue']})


if __name__ == '_main_':
    filename = "customer_orders.csv"
    orders = read_customer_orders(filename)

    if not orders:
        exit(1)

    total_revenue(orders)
    most_popular_product(orders)
    average_price(orders)
    top_products_by_revenue(orders)
    write_product_summary(orders, "product_summary.csv")
