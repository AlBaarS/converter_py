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

# Distance class
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

# Area class
class AreaConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "square_micrometer": 1e12,
        "square_millimeter": 1e6,
        "square_centimeter": 1e4,
        "square_decimeter": 1e2,
        "square_meter": 1,
        "square_decameter": 1e-2,
        "hectare": 1e-4,
        "square_kilometer": 1e-6,
        "square_inch": 1.5500031e3,
        "square_foot": 10.763910417,
        "square_yard": 1.1959900463,
        "acre": 2.471054e-4,
        "square_mile": 3.861018768e-7
    }

# Volume class
class VolumeConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "nanoliter": 1e9,
        "microliter": 1e6,
        "milliliter": 1e3,
        "liter": 1,
        "cubic_meter": 1e-3,
        "cubic_kilometer": 1e-12,
        "fluid_ounce": 33.814038638,
        "cup": 4.2267548297,
        "pint": 2.1133774149,
        "quart": 1.0566887074,
        "gallon": 0.2641721769
    }

# Weight class
class WeightConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "nanogram": 1e12,
        "microgram": 1e9,
        "milligram": 1e6,
        "gram": 1e3,
        "kilogram": 1,
        "metric_ton": 1e-3,
        "ounce": 35.273990723,
        "pound": 2.2046244202,
        "short_ton": 1.1023122e-3,
        "long_ton": 9.842073e-4
    }

# Time class
class TimeConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "picosecond": 3.6e15,
        "nanosecond": 3.6e12,
        "microsecond": 3.6e9,
        "millisecond": 3.6e6,
        "second": 3.6e3,
        "minute": 60,
        "hour": 1,
        "day": 1/24,
        "week": 1/168,
        "month": 1.3689254e-3,
        "year": 1.140771e-4
    }

# Temperature class (future)
