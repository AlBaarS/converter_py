from .base_converter import BaseConverter

class AreaConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "square_micrometer": 1e12,
        "square_millimeter": 1e6,
        "square_centimeter": 1e4,
        "square_decimeter": 1e2,
        "square_meter": 1,
        "square_decameter": 1e-2,
        "hectare": 1e-4,
        "square_kilometer": 1e-6,
        "square_inch": 1.5500031e3,
        "square_foot": 10.763910417,
        "square_yard": 1.1959900463,
        "acre": 2.471054e-4,
        "square_mile": 3.861018768e-7
    }
