class NoUnitFoundError(Exception):
    """Exception raised when the input string does not contain a (valid) unit string

    Attributes:
        message -- explanation of the error
    """

    message: str = """
No valid unit string was found in your input string.
Make sure that your input follows the required format: <value><input_unit> to <output_unit>
Examples:
    convert.py 2.4m to ft
    convert.py 1.2 l to cup
    convert.py 40 square meters to square feet
    """
    error_code: int = 1
  
    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
