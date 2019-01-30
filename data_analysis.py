import glob
import errno
import os
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def get_files():
    path = "{}/data/in/*.dat".format(os.environ["HOME"])
    return glob.glob(path)


def read_file(file):
    content = []
    try:
        with open(file) as f:
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
    collection = {'salesmans': [], 'clients': [], 'sales': []}
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

    return {
        'clients': len(collection['clients']),
        'salesmans': len(collection['salesmans']),
        'expensive': int(expensive[0]),
        'worst': ranking[0][0]
    }


def generate_report(file, report):
    path = "{}/data/in/".format(os.environ["HOME"])
    out_path = "{}/data/out/".format(os.environ["HOME"])
    filename = file.replace(path, '').replace('.dat', '.done.dat')
    output = out_path + filename

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    file = open(output, 'w+')
    file.write("Amount of clients: %s \n" % report['clients'])
    file.write("Amount of salesman: %s \n" % report['salesmans'])
    file.write("ID of the most expensive sale: %s \n" % report['expensive'])
    file.write("Worst salesman ever: %s \n" % report['worst'])
    file.close()


def analysis():
    files = get_files()

    for file in files:
        data = read_file(file)
        report = get_report_data(data)
        generate_report(file, report)

    os.system('clear')
    print("Relatórios finalizado!")


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
                sleep(5)
        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None
        else:
            print("Atualizando relatórios")
            sleep(1)
            analysis()


if __name__ == '__main__':
    w = Watcher()
    w.run()
