import glob
import errno
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def read_files():
    path = "{}/data/in/*.dat".format(os.environ["HOME"])
    files = glob.glob(path)
    content = []
    for name in files:
        try:
            with open(name) as f:
                for line in f:
                    content.append(line)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                print("Ops, ocorreu um erro na leitura dos dados!")

    return content


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
    for seller in salesmans:
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


def get_report_data(data):
    collection = parse_data(data)
    ranking = ranking_salesman(collection['sales'], collection['salesmans'])
    expensive = expensive_sale(collection['sales'])
    os.system('clear')

    return {
        'clients': len(collection['clients']),
        'salesmans': len(collection['salesmans']),
        'expensive': int(expensive[0]),
        'worst': ranking[0][0]
    }


def generate_report(report):
    print("Amount of clients: ", report['clients'])
    print("Amount of salesman: ", report['salesmans'])
    print("ID of the most expensive sale: ", report['expensive'])
    print("Worst salesman ever: ", report['worst'])


def analysis():
    data = read_files()
    report = get_report_data(data)
    return generate_report(report)


class Watcher:
    path = "{}/data/in/".format(os.environ["HOME"])

    analysis()

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.path)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None
        else:
            analysis()


if __name__ == '__main__':
    w = Watcher()
    w.run()
