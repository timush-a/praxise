import csv
import os
import json


class Convert:
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

    def creating_dict_from_csv(self) -> dict:
        """
            Create dict from csv file.
            Returns key, and sorted values.
        """
        dictionary = {}
        for row in self.__read_csv():
            if dictionary.get(row[0]):
                dictionary[row[0]].append((row[1], row[2]))
            else:
                dictionary[row[0]] = [(row[1], row[2])]

        for key, value in dictionary.items():
            dictionary[key] = sorted(value, key=lambda x: x[1], reverse=True)

        return dictionary


class Driver:
    def __init__(self, csv_file: str, db_name='db'):
        self.db_name = db_name
        self.csv_file = csv_file
        self.data = None

    def create_storage(self):
        obj = Convert(self.csv_file)
        with open(f'{self.db_name}.json', 'w') as db:
            db.write(json.dumps(obj.creating_dict_from_csv()))
        print('Storage created')

    def load_storage(self):
        if not os.path.exists(f'{self.db_name}.json'):
            print("File doesn't exist.\n"
                  "Wait until database is creating")
            self.create_storage()
            self.load_storage()
            print('Storage is loaded')
        self.data = json.loads(open(f'{self.db_name}.json').read())
        return self.data

    def select(self, key: str, threshold=0):
        try:
            result = [a[0] for a in filter(
                lambda i: float(i[1]) >= threshold, self.data.get(key))]
            return json.dumps({f'Recommended goods list for {key}': ', '.join(result)})
        except (TypeError, AttributeError):
            return json.dumps(f'Key {key} not found')
