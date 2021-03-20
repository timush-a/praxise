import os
import shelve
import csv


class Converter:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def __read_csv(self) -> tuple:
        """
            Read csv file, and return it line by line.
        """
        with open(self.csv_file) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].isspace():
                    raise StopIteration
                yield row

    def creating_dict_from_csv(self) -> tuple:
        """
            Create dict from csv file.
            Returns key, and sorted values.
        """
        dictionary = {}
        for row in self.__read_csv():
            if dictionary.get(row[0]):
                dictionary[row[0]].append([row[1], row[2]])
            else:
                dictionary[row[0]] = [[row[1], row[2]]]

        for key, value in dictionary.items():
            yield key, sorted(value, key=lambda x: x[1], reverse=True)


class StorageDriver:
    def __init__(self, csv_file: str, db_name='db'):
        self.db_name = db_name
        self.csv_file = csv_file
        self.data = None

    def create_storage(self):
        obj = Converter(self.csv_file)
        with shelve.open(self.db_name) as db:
            for key, value in obj.creating_dict_from_csv():
                db[key] = value
        print('Storage created')

    def load_storage(self):
        if not os.path.exists(f'{self.db_name}.db'):
            print("File doesn't exist.\n"
                  "Wait until database is creating")
            self.create_storage()
            self.load_storage()
            print('Storage is loaded')
        self.data = shelve.open(self.db_name, 'r')

    def select(self, key: str, threshold=0):
        try:
            return [product for product in filter(
                lambda i: float(i[1]) >= threshold, self.data.get(key))]
        except (TypeError, AttributeError):
            return None
