import json
import string
import random as rnd
import datetime as dt


class DataLoader():
    """
    Data Loader. Loads data from json file or from Simulation

    Methods
    -------
    load_data()
        Loads data from json file or from Simulation
    """

    def __init__(self, source: str):
        """
        Parameters
        ----------
        source: str
            The source for data ingestion. Must be either of 'File' or 'Simulation'

        Returns
        -------
        object
            A Data Loader object
        """

        self.source = source

    def load_data(self):
        """
        Loads data from json file or from Simulation

        Returns
        -------
        list
            Loaded data as json array

        Raises
        ------
        ValueError
            If configured 'source' is neither 'File' nor 'Simulation'

        """

        if self.source == 'File':
            return self._read_source_file()
        elif self.source == 'Simulation':
            return self._read_source_simulation()
        else:
            raise ValueError("source type must be either of 'File' or 'Simulation'!")

    @staticmethod
    def _read_file_path():
        # ../data/data.json     --> Location of test source file
        return input("Please insert path plus filename here, in format 'C:\\MyFiles\\data.json': ")

    def _read_source_file(self):
        try:
            filename = self._read_file_path()

            with open(filename, 'r', encoding="utf8") as file:
                json_file = json.load(file)

            return json_file

        except:
            raise ValueError("Please provide a valid path to a json source file!")

    @staticmethod
    def _read_source_simulation():
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
