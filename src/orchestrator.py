# Import modules
from re import Match, match, search, split

# Import exceptions
from src.exceptions.invalid_number_of_input_items import InvalidNumberOfInputArgumentsError
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError
from src.exceptions.incompatible_units import IncompatibleUnits

# Import converters
from src.converters.area_converter import AreaConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

class Orchestrator:

    def __input_handler(self, command: str) -> tuple[float, str, str, int]:

        number_match: str = r"\d+\.\d+|\d+"
        string_match: str = r"[a-zA-Z]+[\s_][a-zA-Z]+|[a-zA-Z]+"

        input_split: list[str] = split("to", command)
        if len(input_split) != 2:
            raise InvalidNumberOfInputArgumentsError()

        input_value_match: Match[str] | None = match(number_match, input_split[0]) # match ensures it starts with a number
        input_unit_match: Match[str] | None = search(string_match, input_split[0]) # search searches through the whole input string
        output_unit_match: Match[str] | None = search(string_match, input_split[1])

        if input_value_match != None:
            input_value: float = float(input_value_match.group().strip())
        else:
            raise NoNumberFoundError()
        if input_unit_match != None:
            input_unit: str = input_unit_match.group().strip()
        else:
            raise NoUnitFoundError()
        if output_unit_match != None:
            output_unit: str = output_unit_match.group().strip()
        else:
            raise NoUnitFoundError()
        
        if len(input_unit) > 2 and input_unit.endswith('s'):
            input_unit: str = input_unit[:-1]
        if len(output_unit) > 2 and output_unit.endswith('s'):
            output_unit: str = output_unit[:-1]
        
        return (input_value, input_unit, output_unit)
    
    def __which_unit(self, unit: str) -> tuple[str, str]:
        out_unit: tuple[str, str] = ('','')
        for found_unit in [
                AreaConverter().which_unit(unit),
                DistanceConverter().which_unit(unit),
                TimeConverter().which_unit(unit),
                VolumeConverter().which_unit(unit),
                WeightConverter().which_unit(unit)
            ]:
            if found_unit[0] != '':
                out_unit: tuple[str, str] = found_unit
        if out_unit[0] != '':
            return out_unit
        else:
            raise NoUnitFoundError()
        
    def __round(self, value: float, decimals: int) -> float | int:
        if decimals > -1:
            rounded_value: float = round(value, decimals)
        else:
            rounded_value: float = value
        if rounded_value == int(rounded_value):
            return int(rounded_value)
        else:
            return rounded_value

    def convert(self, command: str, decimals: int) -> str | None:
        # Process input
        input_split: tuple[float, str, str] = self.__input_handler(command)
        input_value: float = input_split[0]
        input_unit_and_type: tuple[str, str] = self.__which_unit(input_split[1])
        output_unit_and_type: tuple[str, str] = self.__which_unit(input_split[2])

        # Reserve variables for input
        input_unit: str = ""
        output_unit: str = ""
        unit_type: str = ""

        # Sort the input data
        if input_unit_and_type[1] != output_unit_and_type[1]:
            raise IncompatibleUnits(f"{input_unit_and_type[0]} ({input_split[1]})", f"{output_unit_and_type[0]} ({input_split[2]})")
        else:
            input_unit: str = input_unit_and_type[0]
            output_unit: str = output_unit_and_type[0]
            unit_type: str = input_unit_and_type[1]

        # Apply the correct conversion method
        for ConverterClass in [AreaConverter, DistanceConverter, TimeConverter, VolumeConverter, WeightConverter]:
            if ConverterClass().type == unit_type:
                output_value: float = ConverterClass().convert(input_value, input_unit, output_unit)
                output_symbol: str = ConverterClass.units[output_unit][0]
                if output_value != 1:
                    output_unit: str = output_unit + 's'
                return f"{str(self.__round(output_value, decimals))} {output_unit.replace("_", " ")} ({output_symbol})"
