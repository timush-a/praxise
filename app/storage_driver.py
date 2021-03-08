import shelve
import csv


class StorageDriver:
    @staticmethod
    def __read_csv(csv_file_name: str) -> dict:
        """
            Reads the csv file and convert it to dictionary.
        """
        temp = {}
        with open(csv_file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    if temp.get(row[0]):
                        temp[row[0]].append((row[1], row[2]))
                    else:
                        temp[row[0]] = [(row[1], row[2])]

        for key in temp:
            temp[key] = sorted(temp[key], key=lambda x: x[1], reverse=True)

        return temp

    @staticmethod
    def create(csv_file_name: str, db_name: str):
        with shelve.open(db_name, 'c') as db:
          db.update(StorageDriver.__read_csv(csv_file_name))
        return None

    @staticmethod
    def select(data, value: str, threshold=0):
        if data.get(value):
            return f'{[a[0] for a in list(filter(lambda i: float(i[1]) >= threshold, data.get(value)))]}'
        return None
