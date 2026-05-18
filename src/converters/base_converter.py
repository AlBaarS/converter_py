class BaseConverter:

    conversion_multiplier: dict[str, float] = {
        "base": 1,
        "double": 2
    }

    def __str__(self) -> str:
        return str(self.conversion_multiplier)

    def convert(self, number: float, input_unit: str, output_unit: str) -> float:
        multiplier: float = self.conversion_multiplier[output_unit] / self.conversion_multiplier[input_unit]
        return number * multiplier
