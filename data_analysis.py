def calculate_sale(sale):
    soma = 0
    items = sale.replace('[', '').replace(']', '')
    for item in items.split(','):
        (id, quantity, value) = item.split('-')
        soma += (int(quantity) * float(value))

    return soma


def parse_salesman(salesman):
    # [cpf, name, salary]
    return salesman.replace('\n', '').split('ç')[1:]


def parse_client(client):
    # [cnpj, name, type]
    return client.replace('\n', '').split('ç')[1:]


def parse_sale(data):
    # [id, sum, salesman]
    sale = data.replace('\n', '').split('ç')[1:]
    sale[1] = calculate_sale(sale[1])
    return sale


def ranking_salesman(sales, salesmans):
    ranking = {}
    for seller in salesmans[0]:
        ranking[seller[1]] = 0
        for sale in sales:
            if seller[1] == sale[2]:
                ranking[seller[1]] += sale[1]

    return sorted(ranking.items(), key=lambda x: x[1])


def expensive_sale(sales):
    expensive = sales[0]

    for sale in sales:
        if sale[1] > expensive[1]:
            expensive = sale

    return expensive


def parse_data(data):
    collection = {'salesmans': [], 'clients': [], 'sales': [] }
    for row in data:
        if row[:3] == '001':
            collection['salesmans'].append(parse_salesman(row))
        elif row[:3] == '002':
            collection['clients'].append(parse_client(row))
        elif row[:3] == '003':
            collection['sales'].append(parse_sale(row))
    return collection
