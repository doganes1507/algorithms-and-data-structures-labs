import csv


def read_sales_data(file_path):
    sales_data = {}
    file = open(file_path, encoding='utf-8')
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        row = row[0].split(';')
        order_number = row[0]
        order_date = row[1]
        product_name = row[2]
        product_category = row[3]
        quantity = int(row[4])
        unit_price = int(row[5])
        total_price = int(row[6])

        sales_data[product_name] = {
            'order_number': order_number,
            'order_date': order_date,
            'category': product_category,
            'quantity': quantity,
            'price': unit_price,
            'revenue': total_price
        }

    return sales_data


def calculate_revenue(sales_data):
    result = 0

    for product in sales_data:
        result += sales_data[product]['revenue']

    return result


def find_products_with_highest_revenue(sales_data):
    revenues = [sales_data[product]['revenue'] for product in sales_data]
    result = []

    for product in sales_data:
        if sales_data[product]['revenue'] == max(revenues):
            result.append(product)

    return result


def find_products_with_most_sales(sales_data):
    quantities = [sales_data[product]['quantity'] for product in sales_data]
    result = []

    for product in sales_data:
        if sales_data[product]['quantity'] == max(quantities):
            result.append(product)

    return result


def generate_sales_report(sales_data):
    total_revenue = calculate_revenue(sales_data)

    result = f'Total revenue: {total_revenue}\n' \
             f"Product, it's revenue and it's share in total revenue:\n"

    for product in sales_data:
        result += f'{product}: '
        result += f"{sales_data[product]['revenue']} "
        result += f"({round(sales_data[product]['revenue'] / (total_revenue / 100), 5)} %)\n"

    return result


sales_data = read_sales_data('test_table.csv')

print('Total revenue:', calculate_revenue(sales_data))
print('Products with highest revenue:', ', '.join(find_products_with_highest_revenue(sales_data)))
print('Products with most sales:', ', '.join(find_products_with_most_sales(sales_data)))
print(generate_sales_report(sales_data))
