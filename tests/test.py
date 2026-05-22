#!/bin/python3

from src.converters.area_converter import AreaConverter
from src.converters.base_converter import BaseConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

import unittest

class TestConverterObjects(unittest.TestCase):

    def test_doubling(self):
        input_number: float = 21
        output_expect: float = 42
        output_test: float = BaseConverter().convert(input_number, "base", "half")
        self.assertEqual(output_expect, output_test)

    def test_meter_to_centimeter(self):
        input_number: float = 0.42
        output_expect: float = 42
        output_test: float = DistanceConverter().convert(input_number, "meter", "centimeter")
        self.assertEqual(output_expect, output_test)

    def test_feet_to_meter(self):
        input_number: float = 137.79527559
        output_expect: float = 42
        output_test: float = DistanceConverter().convert(input_number, "foot", "meter")
        self.assertAlmostEqual(output_expect, output_test)

    def test_hour_to_day(self):
        input_number: float = 48
        output_expect: float = 2
        output_test: float = TimeConverter().convert(input_number, "hour", "day")
        self.assertAlmostEqual(output_expect, output_test)

    def test_if_symbol_can_be_found(self):
        input_symbol: str = "hf"
        output_expect: str = "half"
        output_test: str = BaseConverter().which_unit(input_symbol)
        self.assertEqual(output_expect, output_test)

    def test_if_symbol_that_is_not_present_returns_an_empty_string(self):
        input_symbol: str = "foo"
        output_expect: str = ""
        output_test: str = BaseConverter().which_unit(input_symbol)
        self.assertEqual(output_expect, output_test)

    def test_if_there_are_duplicate_unit_definitions(self):
        all_units: list[str] = []
        duplicates: list[str] = []
        for category in [AreaConverter().list_units(), DistanceConverter().list_units(), TimeConverter().list_units(), VolumeConverter().list_units(), WeightConverter().list_units()]:
            for unit_definitions in category.values():
                for unit in unit_definitions:
                    if unit in all_units:
                        duplicates.append(unit)
                    else:
                        all_units.append(unit)
        self.assertEqual(duplicates, [])

if __name__ == '__main__':
    unittest.main()
