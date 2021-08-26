class DataOutputer():
    """
    Data Outputer. Sends processed data to specified sink

    Methods
    _______
    save_data()
        Outputs data to configured sink
    """

    def __init__(self, data_contents, target):
        """
        Parameters
        ----------
        data_contents: list
            Final transformed data
        target: str
            The target for data output. Must be either of 'Console' or 'PostgreSQL'
        """
        self.data_contents = data_contents
        self.target = target

    def save_data(self):
        """
        Outputs data to configured sink

        Raises
        ------
        ValueError
            If configured 'target' is neither 'Console' nor 'PostgreSQL'
        """

        if self.target == 'Console':
            self._output_to_console()
        elif self.target == 'PostgreSQL'.capitalize():
            self._output_to_postgres()
        else:
            raise ValueError("sink type must be either of 'Console' or 'PostgreSQL'!")

    def _output_to_console(self):
        print(self.data_contents)
        for line in self.data_contents:
            k = line['key']
            v = line['value']
            ts = line['ts']
            print(f"Current line: key = {k}, value = {v}, and timestamp = {ts}")
            print("=======================")

    def _output_to_postgres(self):
        print(self.data_contents)
        print("Saving data to PostgreSQL database...")
