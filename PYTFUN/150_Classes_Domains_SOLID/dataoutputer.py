class DataOutputer():
    def __init__(self, data_contents, target):
        self.data_contents = data_contents
        self.target = target

    def save_data(self):
        if self.target == 'Console':
            self.output_to_console()
        elif self.target == 'PostgreSQL'.capitalize():
            self.output_to_postgres()
        else:
            raise ValueError("sink type must be either of 'Console' or 'PostgreSQL'!")

    def output_to_console(self):
        print(self.data_contents)
        for line in self.data_contents:
            k = line['key']
            v = line['value']
            ts = line['ts']
            print(f"Current line: key = {k}, value = {v}, and timestamp = {ts}")
            print("=======================")

    def output_to_postgres(self):
        print(self.data_contents)
        print("Saving data to PostgreSQL database...")
