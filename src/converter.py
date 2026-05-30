# Import exceptions
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError

# Import converters
from src.converters.area_converter import AreaConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

def converter(input: tuple[float, str, str]) -> str:
    input_unit: str = ''
    output_unit: str = ''
    for found_input_unit in [AreaConverter().which_unit(input[1]), DistanceConverter().which_unit(input[1]), TimeConverter().which_unit(input[1]), VolumeConverter().which_unit(input[1]), WeightConverter().which_unit(input[1])]:
        if found_input_unit != '':
            input_unit: str = found_input_unit
