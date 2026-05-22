"""Supported input examples
convert.py 2.4m to ft
convert.py 1.2 l to cup
convert.py 40 square meters to square feet
"""

from re import Match, match, search, split
from src.exceptions.invalid_number_of_input_items import InvalidNumberOfInputArgumentsError
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError

def input_handler(command: str) -> tuple[float, str, str]:
    input_split: list[str] = split("to", command)
    if len(input_split) != 2:
        raise InvalidNumberOfInputArgumentsError()
    
    number_match: Match[str] | None = match(r"\d+\.\d+|\d+", input_split[0]) # match ensures it starts with a number
    string_match: Match[str] | None = search(r"[a-zA-Z\s]+", input_split[0]) # search searches through the whole string

    if number_match != None:
        input_value: float = float(number_match.group().strip())
    else:
        raise NoNumberFoundError()
    if string_match != None:
        input_unit: str = string_match.group().strip()
    else:
        raise NoUnitFoundError()
    if input_split[1] != "":
        output_unit: str = input_split[1].strip()
    else:
        raise NoUnitFoundError()
    
    return (input_value, input_unit, output_unit)
