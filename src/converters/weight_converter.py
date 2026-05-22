from .base_converter import BaseConverter

class WeightConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "nanogram":   1e12,
        "microgram":  1e9,
        "milligram":  1e6,
        "gram":       1e3,
        "kilogram":   1,
        "metric_ton": 1e-3,
        "ounce":      35.273990723,
        "pound":      2.2046244202,
        "short_ton":  1.1023122e-3,
        "long_ton":   9.842073e-4
    }
