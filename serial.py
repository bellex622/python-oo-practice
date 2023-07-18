class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # constructor

    def __init__(self, start):
        """Create an instance with a start number"""
        self.start = start
        self.next_number = start

    def generate(self):
        """Increment the next_number by 1, return next_number-1"""
        self.next_number = self.next_number + 1
        return self.next_number - 1

    def reset(self):
        """reset the next_number to be the original number"""
        self.next_number = self.start

    def __repr__(self):
        return f"start = {self.start} and result = {self.next_number}"
