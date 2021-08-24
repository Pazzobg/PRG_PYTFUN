from dataloader import DataLoader
from dataoutputer import DataOutputer


def run():
    data_source = input("Please select data source type ('File' or 'Simulation'): ").capitalize()
    data_sink = input("Please select data sink type ('Console' or 'PostgreSQL'): ").capitalize()

    data_loader = DataLoader(source=data_source)

    json_data = data_loader.load_data()

    outputer = DataOutputer(data_contents=json_data, target=data_sink)

    outputer.save_data()


if __name__ == '__main__':
    run()
