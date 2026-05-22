from .base_converter import BaseConverter

class TimeConverter(BaseConverter):

    conversion_multiplier: dict[str, float] = {
        "picosecond":  3.6e15,
        "nanosecond":  3.6e12,
        "microsecond": 3.6e9,
        "millisecond": 3.6e6,
        "second":      3.6e3,
        "minute":      60,
        "hour":        1,
        "day":         1/24,
        "week":        1/168,
        "month":       1.3689254e-3,
        "year":        1.140771e-4
    }
