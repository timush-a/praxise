import pytest
from storage_driver import StorageDriver


dict_with_one_key = {'WP260qJAo6': [('kLKQ5aYQ4x', '1.0'), ('1HLh2DAzA1', '1.0'),
                                    ('klTPb8MaPT', '0.9'), ('0rOFpWfWE0', '0.9'),
                                    ('iwNVCUXg9Y', '0.9'), ('5XTltK0NNv', '0.9'),
                                    ('iH8r2j0AfA', '0.9'), ('HOBWufKPQd', '0.8'),
                                    ('X4ozUZh2wk', '0.8'), ('eWktrUXixw', '0.8'),
                                    ('rQ8OPSOIes', '0.8'), ('sK2RIPFZ3z', '0.8'),
                                    ('PXrc90Ddlh', '0.8'), ('yj2Pa9SUKl', '0.8'),
                                    ('rxUqVq3ZEL', '0.8'), ('d5DlwGhaCh', '0.8'),
                                    ('uEtX0moHVO', '0.8'), ('mLGlFta6vr', '0.7'),
                                    ('wYgx4gNA8N', '0.7'), ('mvXZyvTD8M', '0.7'),
                                    ('LaB96mR3qw', '0.7'), ('ihiZGUIa3L', '0.7'),
                                    ('nQvVcJ3ftW', '0.7'), ('6GH5DziXeo', '0.7'),
                                    ('zmEYaHYHw2', '0.7'), ('WVnI3JvhRC', '0.7')]}


class TestStorageDriver:
    def test_case_empty(self):
        assert StorageDriver.select({}, '') == None

    def test_case_simple_dict(self):
        with pytest.raises(TypeError):
            assert StorageDriver.select({'key': 1}, 'key', 0.9)

    def test_case_dict_with_one_key(self):
        assert StorageDriver.select(dict_with_one_key,
                                    'WP260qJAo6',
                                    0.9) == ['kLKQ5aYQ4x',
                                             '1HLh2DAzA1',
                                             'klTPb8MaPT',
                                             '0rOFpWfWE0',
                                             'iwNVCUXg9Y',
                                             '5XTltK0NNv',
                                             'iH8r2j0AfA']
