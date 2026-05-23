#!/bin/python3

# Import converters
from src.converters.area_converter import AreaConverter
from src.converters.base_converter import BaseConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

# Import input functions
from src.input.input_handling import input_handler

# Import exceptions
from src.exceptions.invalid_number_of_input_items import InvalidNumberOfInputArgumentsError
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError

# Import python modules
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

class TestInputHandlerFunctions(unittest.TestCase):
    def test_if_input_handler_returns_a_correct_tuple_in_happy_paths(self):
        input_command_fmt1: str = "2.4m to ft"
        input_command_fmt2: str = "1.2 l to cup"
        input_command_fmt3: str = "40 square meters to square feet"
        output_expect_fmt1: tuple[float, str, str] = (2.4, "m", "ft")
        output_expect_fmt2: tuple[float, str, str] = (1.2, "l", "cup")
        output_expect_fmt3: tuple[float, str, str] = (40, "square meters", "square feet")
        output_test_fmt1: tuple[float, str, str] = input_handler(input_command_fmt1)
        output_test_fmt2: tuple[float, str, str] = input_handler(input_command_fmt2)
        output_test_fmt3: tuple[float, str, str] = input_handler(input_command_fmt3)
        self.assertEqual(output_expect_fmt1, output_test_fmt1)
        self.assertEqual(output_expect_fmt2, output_test_fmt2)
        self.assertEqual(output_expect_fmt3, output_test_fmt3)

    def test_if_multiple_to_results_in_InvaludNumberOfInputArgumentsError(self):
        input_command: str = "to be or not to be that is the question"
        self.assertRaises(InvalidNumberOfInputArgumentsError, input_handler, input_command)

    def test_if_a_string_at_the_start_results_in_a_NoNumberFoundError(self):
        input_command: str = "please convert 40 square meters to square feet"
        self.assertRaises(NoNumberFoundError, input_handler, input_command)

    def test_if_the_first_number_is_selected_when_multiple_are_submitted(self):
        input_command: str = "40 5.3 69 square meters to square feet"
        output_expect: tuple[float, str, str] = (40, "square meters", "square feet")
        output_test: tuple[float, str, str] = input_handler(input_command)
        self.assertEqual(output_expect, output_test)

    def test_if_multiple_strings_as_unit_are_handled_correctly(self):
        input_command: str = "40 square meters bilbo baggins to square feet"
        output_expect: tuple[float, str, str] = (40, "square meters", "square feet")
        output_test: tuple[float, str, str] = input_handler(input_command)
        self.assertEqual(output_expect, output_test)

if __name__ == '__main__':
    unittest.main()
