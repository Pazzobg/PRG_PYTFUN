# You are creating a pseudo-ETL system, which needs to be able to retrieve data from various sources and transmit the
# data to various sinks. By data we mean short json messages with predefined structure. Here is an example:
#
# {"key": "A123", "value":"15.6", "ts":'2020-10-07 13:28:43.399620+02:00'}
#
# You need to implement at least the following functionality:
# * Data source is Simulation: this source will generate random data.
# * Data source is File: the messages are read from an input file which contains a json array of messages.
# * Data sink is Console: the consumed messages are printed to stdout.
# * Data sink is PostgreSQL: the consumed messages are inserted in a database table in PostgreSQL
# * Messages should be read and transmitted one by one until the source has no more messages.
#   The Simulation source is infinite - it should always have a new message, if asked.
#   The File source is finite, it ends when the whole file is read.
#
# If you right actual code, make your interface as user-friendly as possible, e.g. make it fluent :
#
# ETL().source(source_args).sink(sink_args).run()

import threading
import json
import string
import random as rnd
import datetime as dt


def load_data(source):
    # ../data/data.json     --> Location of test source file
    if source == 'File':
        return read_source_file()
    elif source == 'Simulation':
        return read_source_simulation()
    else:
        raise ValueError("source type must be either of 'File' or 'Simulation'!")


def read_source_file():
    try:
        filename = input("Please insert path plus filename here, in format 'C:\\MyFiles\\data.json': ")

        with open(filename, 'r', encoding="utf8") as file:
            json_file = json.load(file)

        return json_file

    except:
        raise ValueError("Please provide a valid path to a json source file!")


def read_source_simulation():
    output = []

    key_letter = rnd.choices(string.ascii_uppercase, k=1)[0]    # random.choices returns a list[]
    key_nums = ''.join(rnd.choices(string.digits, k=3))
    k = f'{key_letter}{key_nums}'

    v = round(rnd.uniform(-20, 40), 1)

    end = dt.datetime.now(dt.timezone.utc)
    dte = end - dt.timedelta(rnd.randint(1, 1500))
    ts = f"{dte.strftime('%Y-%m-%d %H:%M:%S.%f%z')}"

    out_str = f'{{"key": "{k}", "value": "{v}", "ts": "{ts}"}}'

    output.append(json.loads(out_str))
    return output


def save_data(data_contents, destination):
    if destination == 'Console':
        output_to_console(data_contents)
    elif destination == 'PostgreSQL'.capitalize():
        output_to_postgres(data_contents)
    else:
        raise ValueError("sink type must be either of 'Console' or 'PostgreSQL'!")


def output_to_console(data_contents):
    print(data_contents)
    for line in data_contents:
        k = line['key']
        v = line['value']
        ts = line['ts']
        print(f"Current line: key = {k}, value = {v}, and timestamp = {ts}")
        print("=======================")


def output_to_postgres(data_contents):
    print(data_contents)
    print("Saving data to PostgreSQL database...")


if __name__ == '__main__':
    data_source = input("Please select data source type ('File' or 'Simulation'): ").capitalize()
    data_sink = input("Please select data sink type ('Console' or 'PostgreSQL'): ").capitalize()

    json_data = load_data(data_source)

    save_data(json_data, data_sink)
