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
    
    return (input_value, input_unit, output_unit)
