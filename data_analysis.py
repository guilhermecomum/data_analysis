def calculate_sale(sale):
    soma = 0
    items = sale.replace('[', '').replace(']', '')
    for item in items.split(','):
        (id, quantity, value) = item.split('-')
        soma += (int(quantity) * float(value))

    return soma


def parse_salesman(salesman):
    return salesman.split('ç')[1:]


def parse_client(client):
    return client.split('ç')[1:]


def parse_sale(data):
    sale = data.split('ç')[1:]
    sale[1] = calculate_sale(sale[1])
    return sale
