class Numfinity:
    """
    <Numfinity: a type of variable that allows to store massive numbers.>
    Copyright (C) 2021  Camilo Franco Moya

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """
    # Atributes
    integralPart = ["0"]
    decimalPart = ["0"]
    negative = False
    original = 0.0

    def __init__(self, negativeSign=False, integral="0", decimal="0"):
        """Create an Numfinity object."""
        self.changeValueByPart(negativeSign, integral, decimal)

    def changeValueByPart(self, negativeSign=False, integral="0", decimal="0"):
        """
        (bool, str, str) -> Numfinity
        precondition: The Strings can only contain numbers, no dot nor sign.
        Use an integral and decimal individual part to change the value.
        Empty strings are equal to "0".
        """
        # Support to empty strings
        if integral == "":
            integral = "0"
        if decimal == "":
            decimal = "0"

        # To ensure that preconditions are met.
        for char in integral:
            assert integral.isdigit(), "{} is invalid.".format(integral)
        for char in decimal:
            assert decimal.isdigit(), "{} is invalid.".format(decimal)

        self.integralPart = Numfinity.convertNumber(integral, False)
        self.decimalPart = Numfinity.convertNumber(decimal, True)

        # If the final value equal to 0.0 (str may have more zeros)
        if float(self) == 0.0:
            # remove the negative sign
            self.negative = False
        else:
            self.negative = negativeSign

        self.original = float(self)

        return self

    def changeValue(self, number=0.0):
        """
        (float) -> Numfinity
        Change the value to another number.
        The integral and decimal part is limited to 15 digits each one.
        Use changeValueByParts to use more digits.
        """
        self.integralPart = Numfinity.convertNumber(str(
            int(number))[-15:], False)
        self.decimalPart = Numfinity.convertNumber(str(
            float(number - int(number)))[2:15], True)

        self.negative = Numfinity.determineSign(number)
        self.original = number

        return self

    @staticmethod
    def convertNumber(number, decimalMode):
        """
        (str, bool) -> list
        Store number sections in a list.
        """
        converted = []

        # if the number is negative or it has invalid values (.)
        if number[0] == "-" or number[0] == ".":
            # remove it
            number = number[1:]

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
                        (counter * -15) - 15:len(number) - (counter * 15)])

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
