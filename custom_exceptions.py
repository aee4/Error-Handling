#A custom exception can be created by inheriting from the "Exception" class
class LegacyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example:
try:
    raise LegacyError("Big Error")
except LegacyError as e:
    print(f"Caught custom exception: {e}")