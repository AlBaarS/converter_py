#!/bin/python3

from src.converters.base_converter import BaseConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
import unittest

class TestConverterObjects(unittest.TestCase):

    def test_doubling(self):
        input_number: float = 21
        output_expect: float = 42
        output_test: float = BaseConverter().convert(input_number, "base", "double")
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

if __name__ == '__main__':
    unittest.main()
