#!/bin/python3

### Input stuff will come here

# Converter classes
class BaseConverter:
    conversion_factors = {
        "base": 1.0,
        "double": 2.0
    }

    def __str__(self):
        return self.conversion_factors

    def convert(self, number: float, input_unit: str, output_unit: str):
        multiplier: float = self.conversion_factors[output_unit] / self.conversion_factors[input_unit]
        return number * multiplier
