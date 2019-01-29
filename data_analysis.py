def calculate_sale(sale):
    soma = 0
    items = sale.replace('[', '').replace(']', '')
    for item in items.split(','):
        (id, quantity, value) = item.split('-')
        soma += (int(quantity) * float(value))

    return soma


def parse_salesman(salesman):
    # [cpf, name, salary]
    return salesman.split('ç')[1:]


def parse_client(client):
    # [cnpj, name, type]
    return client.split('ç')[1:]


def parse_sale(data):
    # [id, sum, salesman]
    sale = data.split('ç')[1:]
    sale[1] = calculate_sale(sale[1])
    return sale


def ranking_salesman(sales, salesmans):
    ranking = {}
    parsed_salesmans = salesmans_collection(salesmans)
    parsed_sales = sales_collection(sales)

    for seller in parsed_salesmans:
        ranking[seller[1]] = 0
        for sale in parsed_sales:
            if seller[1] == sale[2]:
                ranking[seller[1]] += sale[1]

    return sorted(ranking.items(), key=lambda x: x[1])


def expensive_sale(sales):
    parsed_sales = sales_collection(sales)

    expensive = parsed_sales[0]

    for sale in parsed_sales:
        if sale[1] > expensive[1]:
            expensive = sale

    return expensive


def sales_collection(sales):
    parsed_sales = []

    for sale in sales:
        parsed_sales.append(parse_sale(sale))

    return parsed_sales


def salesmans_collection(salesmans):
    parsed_salesmans = []
    for salesman in salesmans:
        parsed_salesmans.append(parse_salesman(salesman))

    return parsed_salesmans
