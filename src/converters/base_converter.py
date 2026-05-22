class BaseConverter:

    conversion_multiplier: dict[str, float] = {
        "base":   1,
        "double": 2
    }

    units: dict[str, list[str]] = {
        "base":   ["b","bs","base"],
        "double": ["d","db","double"]
    }

    def __str__(self) -> str:
        return str(self.conversion_multiplier)

    def convert(self, number: float, input_unit: str, output_unit: str) -> float:
        multiplier: float = self.conversion_multiplier[output_unit] / self.conversion_multiplier[input_unit]
        return number * multiplier
    
    def which_unit(self, symbol: str) -> str:
        found_unit: str = ""
        for unit, symbol_list in self.units.items():
            if symbol in symbol_list:
                found_unit: str = unit
        return found_unit
