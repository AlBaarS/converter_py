class UnitDeterminator:

    units: dict[str, dict[str, list[str]]] = {
        "area": {
            "square_nanometer":  ["nm²","nm2","nm^2","sqnm","sq_nm","square nanometer","square_nanometer","square nanometre","square_nanometre"],
            "square_micrometer": ["µm²","µm2","µm^2","sqµm","sq_µm","um2","um^2","um²","squm","sq_um","square micrometer","square_micrometer","square micrometre","square_micrometre"],
            "square_millimeter": ["mm²","mm2","mm^2","sqmm","sq_mm","square millimeter","square_millimeter","square millimetre","square_millimetre"],
            "square_centimeter": ["cm²","cm2","cm^2","sqcm","sq_cm","square centimeter","square_centimeter","square centimetre","square_centimetre"],
            "square_decimeter":  ["dm²","dm2","dm^2","sqdm","sq_dm","square decimeter","square_decimeter","square decimetre","square_decimetre"],
            "square_meter":      ["m²","m2","m^2","sqm","sq_m","square meter","square_meter","square metre","square_metre"],
            "square_decameter":  ["dam²","dam2","dam^2","sqdam","sq_dam","square decameter","square_decameter","square decametre","square_decametre"],
            "hectare":           ["ha","hm²","hm2","hm^2","sqhm","sq_hm","square hectometer", "square_hectometer","square hectometre", "square_hectometre"],
            "square_kilometer":  ["km²","km2","km^2","sqkm","sq_km","square kilometer","square_kilometer","square kilometre","square_kilometre"],
            "square_inch":       ["in²","in2","in^2","sqin","sq_in","square inch","square_inch"],
            "square_foot":       ["ft²","ft2","ft^2","sqft","sq_ft","square foot","square_foot"],
            "square_yard":       ["yd²","yd2","yd^2","sqyd","sq_yd","square yard","square_yard"],
            "acre":              ["acre","ac"],
            "square_mile":       ["mi²","mi2","mi^2","sqmi","sq_mi","square mile","square_mile"]
        },
        "distance": {
            "nanometer":     ["nm","nanometer","nanometre"],
            "micrometer":    ["µm","um","micrometer","micrometre"],
            "millimeter":    ["mm","millimeter","millimetre"],
            "centimeter":    ["cm","centimeter","centimetre"],
            "decimeter":     ["dm","decimeter","decimetre"],
            "meter":         ["m","meter","metre"],
            "decameter":     ["dam","decameter","decametre"],
            "hectometer":    ["hm","hectometer","hectometre"],
            "kilometer":     ["km","kilometer","kilometre"],
            "inch":          ["in","inch"],
            "foot":          ["ft","ft.","foot"],
            "yard":          ["yd","yard"],
            "mile":          ["mi","mile"],
            "nautical_mile": ["nmi","nautical mile","nautical_mile"],
            "lightyear":     ["ly","light year","light_year","light-year"]
        },
        "time": {
            "picosecond":  ["ps","picosecond"],
            "nanosecond":  ["ns","nanosecond"],
            "microsecond": ["µs","us","microsecond"],
            "millisecond": ["ms","millisecond"],
            "second":      ["s","sec","second"],
            "minute":      ["mn","min","minute"],
            "hour":        ["hr","hour"],
            "day":         ["dy","day"],
            "week":        ["wk","week"],
            "month":       ["mo","month"],
            "year":        ["yr","year"]
        },
        "volume": {
            "nanoliter":       ["nl","nanoliter","nanolitre"],
            "microliter":      ["µl","ul","microleter","microlitre","mm³","mm3","mm^3","cubic millimeter","cubic_millimeter","cubic millimetre","cubic_millimetre"],
            "milliliter":      ["ml","milliliter","millilitre","cm³","cm3","cm^3","cubic centimeter","cubic_centimeter","cubic centimetre","cubic_centimetre"],
            "liter":           ["l","liter","litre","dm³","dm3","dm^3","cubic decimeter","cubic_decimeter","cubic decimetre","cubic_decimetre"],
            "cubic_meter":     ["m³","m3","m^3","cubic meter","cubic_meter","cubic metre","cubic_metre"],
            "cubic_kilometer": ["km³","km3","km^3","cubic kilometer","cubic_kilometer","cubic kilometre","cubic_kilometre"],
            "fluid_ounce":     ["fl oz","fl_oz","fluid ounce","fluid_ounce"],
            "cup":             ["cup"],
            "pint":            ["pt","p","pint"],
            "quart":           ["qt","quart"],
            "gallon":          ["gal","gallon"]
        },
        "weight": {
            "nanogram":   ["ng","nanogram","nanogramme"],
            "microgram":  ["µg","ug","microgram","microgramme"],
            "milligram":  ["mg","milligram","milligramme"],
            "gram":       ["g","gram","gramme"],
            "kilogram":   ["kg","kilo","kilogram","kilogramme"],
            "metric_ton": ["t","ton","tonne","metric ton","metric_ton","metric tonne","metric_tonne"],
            "ounce":      ["oz","℥","ounce"],
            "pound":      ["lb","pound"],
            "short_ton":  ["st","s_t","short ton","short_ton","short tonne","short_tonne"],
            "long_ton":   ["lt","l_t","long ton","long_ton","long tonne","long_tonne"]
        }
    }

    def __str__(self) -> str:
        return str(self.units)
    
    def list_units(self) -> dict[str, dict[str, list[str]]]:
        return self.units
