#!/bin/python3

### Input stuff will come here

# Converter classes
# Converter Parent class
class BaseConverter:

    conversion_multiplier: dict[str, float] = {
        "base": 1,
        "double": 2
    }

    def __str__(self) -> BaseConverter:
        return self.conversion_multiplier

    def convert(self, number: float, input_unit: str, output_unit: str) -> float:
        multiplier: float = self.conversion_multiplier[output_unit] / self.conversion_multiplier[input_unit]
        return number * multiplier

# Distance Child class
class DistanceConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "nanometer": 1e9,
        "micrometer": 1e6,
        "millimeter": 1e3,
        "centimeter": 1e2,
        "decimeter": 1e1,
        "meter": 1,
        "decameter": 1e-1,
        "hectometer": 1e-2,
        "kilometer": 1e-3,
        "inch": 39.37007874,
        "foot": 3.280839895,
        "yard": 1.0936132983,
        "mile": 6.213712e-4,
        "lightyear": 1.057008707e16
    }

# Area Child class

# Volume Child class

# Weight Child class

# Temperature Class (future)
