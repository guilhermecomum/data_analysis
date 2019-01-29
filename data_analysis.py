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
    parsed_salesmans = []
    parsed_sales = []

    for salesman in salesmans:
        parsed_salesmans.append(parse_salesman(salesman)[1])

    for sale in sales:
        parsed_sales.append(parse_sale(sale))

    for seller in parsed_salesmans:
        ranking[seller] = 0
        for sale in parsed_sales:
            if seller == sale[2]:
                ranking[seller] += sale[1]

    return sorted(ranking.items(), key=lambda x: x[1])


def expensive_sale(sales):
    parsed_sales = []

    for sale in sales:
        parsed_sales.append(parse_sale(sale))

    expensive = parsed_sales[0]

    for sale in parsed_sales:
        if sale[1] > expensive[1]:
            expensive = sale

    return expensive
