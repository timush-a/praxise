import csv
import datetime
import time


class CSVReader:
    """
    Read csv file, and return it as a dictionary.
    It takes up a lot of RAM. Can be used with small files
    """
    @staticmethod
    def read(file_name: str) -> dict:
        storage = {}
        with open(file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    if storage.get(row[0]):
                        storage[row[0]].append([row[1], row[2]])
                    else:
                        storage[row[0]] = [[row[1], row[2]]]

        return storage


class SortDictionaryValues:
    @staticmethod
    def sort(dictionary: dict) -> dict:
        """
            Sorts the values in the dictionary in descending order.
        """
        for key in dictionary:
            dictionary[key] = sorted(dictionary[key], key=lambda x: x[1], reverse=True)
        return dictionary


class Loader:
    file_loaded = False

    @staticmethod
    def load(csv_file_name: str) -> dict:
        """
        Loads a csv file, then converts it to a dictionary.
        After that, it sorts the values in the dictionary in descending order.
        Logs time and result of operations
        """
        start_creation = time.time()
        with open('log.txt', 'a') as f:
            try:
                data = CSVReader.read(csv_file_name)
            except IOError:
                f.write(f'{datetime.datetime.now().strftime("%Y-%h-%d  %H-%M-%S")}'
                        f'\nAn error was found while reading the file')

            try:
                SortDictionaryValues.sort(data)
            except (IndexError, ValueError):
                f.write(f'{datetime.datetime.now().strftime("%Y-%h-%d  %H-%M-%S")}'
                        f'\nAn error was found while sorting dictionary values')

            else:
                elapsed_time = time.strftime('%H:%M:%S', time.localtime(time.time() - start_creation))
                f.write(f'\nFile read successfully, values has been sorted'
                        f'\nElapsed time {elapsed_time}')
                Loader.file_loaded = True

        return data
