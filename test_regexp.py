from regexp import SimpleMathematicalOperationsCalculator as Calculator


one_variable = 'a-=1a+=1a+=10a+=a'

three_variables = 'a=1a=+1a=-1a=ba=b+100a=b-100b+=10b+=+10b+=-10b+=bb+=b+100' \
                  'b+=b-100c-=101c-=+101c-=-101c-=bc-=b+101c-=b-101'

raw_data = 'saf nahu haou fhj sf,aa134%...jfbak fa sd fb+=as;2kl5klskdfsjglknc+=a + 100' \
           'jakjgasf/..klsjgl naemfa-=1000'


class TestCalculator:
    def test_case_empty(self):
        test_case = Calculator('', {'a': 0, 'b': 0, 'c': 0})
        assert test_case.calculate() == {'a': 0, 'b': 0, 'c': 0}

    def test_case_with_one_variable(self):
        test_case = Calculator(one_variable, {'a': 1, 'b': 2, 'c': 3})
        assert test_case.calculate() == {'a': 22, 'b': 2, 'c': 3}

    def test_case_with_three_variables(self):
        test_case = Calculator(three_variables, {'a': 1, 'b': 2, 'c': 3})
        assert test_case.calculate() == {"a": -98, "b": 196, "c": -686}

    def test_case_raw_data(self):
        test_case = Calculator(raw_data, {'a': 100, 'b': -1, 'c': 88})
        assert test_case.calculate() == {'a': -900, 'b': 99, 'c': 188}
