from .base_converter import BaseConverter

class VolumeConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "nanoliter": 1e9,
        "microliter": 1e6,
        "milliliter": 1e3,
        "liter": 1,
        "cubic_meter": 1e-3,
        "cubic_kilometer": 1e-12,
        "fluid_ounce": 33.814038638,
        "cup": 4.2267548297,
        "pint": 2.1133774149,
        "quart": 1.0566887074,
        "gallon": 0.2641721769
    }
