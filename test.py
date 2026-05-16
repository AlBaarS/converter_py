#!/bin/python3

import convert
import unittest

class TestBaseConverterObject(unittest.TestCase):

    def test_doubling(self):
        input_number: float = 21
        output_expect: float = 42
        output_test: float = convert.BaseConverter().convert(input_number, "base", "double")
        self.assertEqual(output_expect, output_test)

class TestDistanceConverterObj(unittest.TestCase):

    def test_meter_to_centimeter(self):
        input_number: float = 0.42
        output_expect: float = 42
        output_test: float = convert.DistanceConverter().convert(input_number, "meter", "centimeter")
        self.assertEqual(output_expect, output_test)

    def test_feet_to_meter(self):
        input_number: float = 137.79527559
        output_expect: float = 42
        output_test: float = convert.DistanceConverter().convert(input_number, "foot", "meter")
        self.assertAlmostEqual(output_expect, output_test)

if __name__ == '__main__':
    unittest.main()
