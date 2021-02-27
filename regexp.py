import re


class SimpleMathematicalOperationsCalculator:
    """
        Search variables and simple arithmetic expressions in text and counting the result of calculations.
        Variable names only a, b and c.
        Mathematical operators that can be found in the text:
        +, -, =, +=, -=
    """
    def __init__(self, text: str, values: dict):
        self.text = text
        self.values = values

    def calculate(self) -> dict:
        matches = re.findall(r"([abc])([+-]?)=([abc]?)([+-]?\d*)", self.text)
        for v1, sign, v2, number in matches:
            right = self.values.get(v2, 0) + int(number or 0)
            if sign == "-":
                self.values[v1] -= right
            elif sign == "+":
                self.values[v1] += right
            else:
                self.values[v1] = right

        return self.values
