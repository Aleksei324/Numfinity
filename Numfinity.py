class Numfinity:
    """docstring for Numfinity."""
    # Atributes
    integralPart = ["0"]
    decimalPart = ["0"]
    negative = False
    original = 0.0

    def __init__(self, number):
        """Create an Numfinity object."""
        self.changeValue(number)

    def changeValue(self, number):
        """
        (float) -> Numfinity
        Change the value to another number.
        The integral and decimal part is limited to 15 digits.
        Use changeValueByParts to use more digits.
        """
        self.integralPart = Numfinity.convertNumber(str(
            int(number))[-15:], False)
        self.decimalPart = Numfinity.convertNumber(str(
            float(number - int(number)))[2:15], True)

        self.negative = Numfinity.determineSign(number)
        self.original = number

        return self

    def changeValueByParts(self, negativeSign, integral, decimal):
        """
        (bool, str, str) -> Numfinity
        Use an integral and decimal individual part to change the value.
        """
        self.integralPart = Numfinity.convertNumber(integral, False)
        self.decimalPart = Numfinity.convertNumber(decimal, True)

        if float(self) == 0.0:
            self.negative = False
        else:
            self.negative = negativeSign

        self.original = float(self)

        return self

    @staticmethod
    def convertNumber(number, decimalMode):
        """
        (str, bool) -> list
        Store number sections in a list.
        """
        converted = []

        # if the number is negative
        if number[0] == "-":
            # remove the negative sign
            number[:] = number[1:]

        # Identify how many elements will be stored in the list
        numItems = len(number) / 15

        # If the quantity of elements is less or equal than 1...
        if numItems <= 1:
            # Add it to the list
            converted.insert(0, number)
        else:
            if decimalMode:
                # count until all the items are added
                for counter in range(int(numItems) + 1):
                    # Get the respective item based on the digits and add it
                    converted.append(number[
                        (counter * 15):(counter * 15) + 15])
            else:
                # count until all the items are added
                for counter in range(int(numItems) + 1):
                    # Get the respective item based on the digits and add it
                    converted.insert(0, number[
                        (counter * -15) - 15:(counter * -15) - 1])

        return converted

    @staticmethod
    def determineSign(number):
        """
        (float) -> bool
        Autodetermine the number sign.
        """
        if number >= 0:
            return False
        else:
            return True

    def __str__(self):
        """
        (Numfinity) -> str
        Convert an Numfinity object to string.
        """
        if self.negative:
            string = "-"
        else:
            string = ""

        for element in self.integralPart:
            string += element

        string += "."

        for element in self.decimalPart:
            string += element

        return string

    def __float__(self):
        """
        (Numfinity) -> float
        Convert an Numfinity object to float.
        if the number is too long, it could lose accuracy.
        """
        return float(str(self))

    def __eq__(self, other):
        """
        (Numfinity, Numfinity) -> bool
        Compare 2 Numfinity objects.
        """
        return str(self) == str(other)
