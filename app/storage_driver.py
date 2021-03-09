from collections import namedtuple
from load_csv import Loader


class StorageDriver:
    @staticmethod
    def create(csv_file_name: str) -> namedtuple:
        temp_dict = Loader.load(csv_file_name)
        temp_tuple = namedtuple('temp_tuple', temp_dict.keys())
        result_tuple = temp_tuple(**temp_dict)
        return result_tuple

    @staticmethod
    def select(data, key: str, threshold=0):
        if data.get(key):
            return [a[0] for a in list(filter(lambda i: float(i[1]) >= threshold, data.get(key)))]
        return None
