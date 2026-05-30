#!/bin/python3
from src.converters.area_converter import AreaConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter
from src.input.input_handler import input_handler

import sys

if __name__ == "__main__":
    input_args: str = " ".join(sys.argv[1:])
    print(input_args)
    input_classified: tuple[float, str, str] = input_handler(input_args)
    print(input_classified)
