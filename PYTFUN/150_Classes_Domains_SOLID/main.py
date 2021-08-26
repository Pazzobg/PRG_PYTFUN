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

from dataloader import DataLoader
from dataoutputer import DataOutputer


# Main processing method
def run():
    # Read the params for desired input/output from the Console
    data_source = input("Please select data source type ('File' or 'Simulation'): ").capitalize()
    data_sink = input("Please select data sink type ('Console' or 'PostgreSQL'): ").capitalize()

    # Instantiate a Data Loader
    data_loader = DataLoader(source=data_source)

    # Load data from the specified source
    json_data = data_loader.load_data()

    # Instantiate Data Outputer
    outputer = DataOutputer(data_contents=json_data, target=data_sink)

    # Send final data to specified sink
    outputer.save_data()


# Program entry point
if __name__ == '__main__':
    run()
