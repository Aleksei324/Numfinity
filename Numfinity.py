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
        Use changeValueByPart for more accuracy.
        """
        number = float(number)
        splitNumber = str(number).split(".")

        self.integralPart = Numfinity.convertNumber(splitNumber[0], False)
        self.decimalPart = Numfinity.convertNumber(splitNumber[1], True)

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

        # if the number is negative
        if number[0] == "-":
            # remove the sign
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

    def __sum__(self, other):
        """
        (Numfinity, ?) -> Numfinity
        Sum 2 objects. (WIP)
        """
        if isinstance(other, Numfinity):
            return Numfinity.sumNumfinity(self, other)

        elif isinstance(other, float):
            return NotImplemented  # TODO: support for floats

        else:
            return NotImplemented

    @ staticmethod
    def sumNumfinity(self, other):
        """
        (Numfinity, Numfinity) -> Numfinity
        Sum 2 Numfinity objects.
        """
        # Store the added values
        convertedIntegral = self.integralPart
        convertedDecimal = self.decimalPart

        # INTEGRAL PART - - -

        # If the second value is negative
        if not(self.negative) and other.negative:
            pass  # TODO: This (Maybe I could call the __sub__)

        # If the first value is negative
        elif self.negative and not(other.negative):
            pass  # TODO: This (Maybe I could call the __sub__)

        # If both sign are equal
        elif self.negative and other.negative or not(
                self.negative) and not(other.negative):

            # If the first object has more elements
            if len(self.integralPart) > len(other.integralPart):
                # Sum it
                Numfinity.sumIntegralNumfinitySameSign(
                    convertedIntegral, convertedDecimal, self.
                    integralpart, other.integralPart, 0)

            # If the second object has more elements
            elif len(self.integralPart) < len(other.integralPart):
                # Sum it
                Numfinity.sumIntegralNumfinitySameSign(
                    convertedIntegral, convertedDecimal, other.
                    integralPart, self.integralPart, 0)

            # If both list have the same quantity of elements
            else:
                # Sum it with this special method
                Numfinity.sumIntegralNumfinitySameSignSameSize(
                    convertedIntegral, convertedDecimal, self.
                    integralPart, other.integralPart)

            # DECIMAL PART - - -

            # If the first object has more elements
            if len(self.decimalPart) > len(other.decimalPart):
                Numfinity.sumDecimalNumfinitySameSign(
                    convertedDecimal, convertedIntegral, self.
                    decimalpart, other.decimalPart, 0)

            # If the second object has more elements
            elif len(self.decimalPart) < len(other.decimalPart):
                Numfinity.sumDecimalNumfinitySameSign(
                    convertedDecimal, convertedIntegral, other.
                    decimalPart, self.decimalPart, 0)

            # If both list have the same quantity of elements
            else:
                # Sum it with this special method
                Numfinity.sumDecimalNumfinitySameSignSameSize(
                    convertedDecimal, convertedIntegral, self.
                    decimalPart, other.decimalPart)

            # Create a new object with the sum
            newNumfinityObject = Numfinity()
            newNumfinityObject.integralPart = convertedIntegral
            newNumfinityObject.decimalPart = convertedDecimal
            newNumfinityObject.negative = self.negative
            newNumfinityObject.original = float(newNumfinityObject)

            return newNumfinityObject

    # INTEGRAL - - -

    @ staticmethod
    def sumIntegralNumfinitySameSign(
            convertedIntegral, convertedDecimal, bigger, smaller, index):
        """
        (list, list, list) -> None
        A method to avoid repeating code in __sum__
        """
        # To have both list with equal size
        for counter in range(len(bigger)):
            if len(bigger) > len(smaller):
                smaller.insert(0, "000000000000000")

        for i in range(len(bigger)):
            # Ignore the loop if the index is bigger
            if index > i:
                continue

            # If the smaller list have only zeros
            if smaller[i] == "000000000000000":
                # Add the residual
                convertedIntegral[i] = str(int(bigger[i]) // (10**15))

            else:
                # Add the residual to the element at the left
                convertedIntegral[i - 1] = str(((int(
                    bigger[i]) + int(smaller[i])) // (10**15))
                    + int(convertedIntegral[i - 1]))

            # Always sum the values until 15 digits
            convertedIntegral[i] = str(int(bigger[i]) + int(
                smaller[i]))[-15:]

        # Remove the zeros
        for i in range(len(smaller) - 1):
            if smaller[i] == "000000000000000":
                smaller.pop(i)
            else:
                break

    @ staticmethod
    def sumIntegralNumfinitySameSignSameSize(
            convertedIntegral, convertedDecimal, list1, list2):
        """
        (list, list, list) -> None
        A method to avoid repeating code in __sum__
        """
        for i, stringElement in enumerate(list1):

            # If the element's number of list1 is bigger
            if stringElement > list2[i]:
                Numfinity.sumIntegralNumfinitySameSign(
                    convertedIntegral, convertedDecimal, list1, list2, i)

            # If the element's number of list1 is smaller
            elif stringElement < list2[i]:
                Numfinity.sumIntegralNumfinitySameSign(
                    convertedIntegral, convertedDecimal, list2, list1, i)

            # If both are equal
            else:
                # If there are no more elements at the left
                if i - 1 == -1:
                    # create a new element and add the residual
                    convertedIntegral.insert(0, str(
                        (2 * int(list1[i])) // (10**15)))

                else:
                    # Add the residual to the element at the left
                    convertedIntegral[i - 1] = str(((2 * int(list1[i])) // (
                        10**15)) + int(convertedIntegral[i - 1]))

                # Always Sum the values until 15 digits
                convertedIntegral[i] = str(2 * int(
                    list1[i]))[-15:]

    # DECIMAL - - -

    @ staticmethod
    def sumDecimalNumfinitySameSign(
            convertedDecimal, convertedIntegral, bigger, smaller, index):
        """
        (list, list, list) -> None
        A method to avoid repeating code in __sum__
        """
        # To have both list with equal size
        for counter in range(len(bigger)):
            if len(bigger) > len(smaller):
                smaller.append("000000000000000")

        for i in range(len(bigger)):
            # Skip if the index is not the correct
            if index > i:
                continue

            # If there are no more elements at the left
            if i - 1 == -1:
                # Add the residual to the last element of the integrals
                convertedIntegral[-1] = str(((int(bigger[i]) + int(
                    smaller[i])) // (10**15)) + int(
                    convertedIntegral[-1]))

                # Sum the values until 15 digits
                convertedDecimal[i] = str(int(bigger[i]) + int(
                    smaller[i]))[-15:]

            else:
                # add the residual to the element at the left
                convertedDecimal[i - 1] = str((int(
                    bigger[i]) + int(smaller[i]) // (10**15))
                    + int(convertedDecimal[i - 1]))

                # Sum the values until 15 digits
                convertedDecimal[i] = str(int(bigger[i]) + int(
                    smaller[i]))[-15:]

        # remove the zeros until it reach the last element with values
        for i in range(len(smaller) - 1, 0, -1):
            if smaller[i] == "000000000000000":
                smaller.pop(i)
            else:
                break

    @staticmethod
    def sumDecimalNumfinitySameSignSameSize(
            convertedDecimal, convertedIntegral, list1, list2):
        """
        (list, list, list) -> None
        A method to avoid repeating code in __sum__
        """
        for i, stringElement in enumerate(list1):

            # If the element's number of list1 is bigger
            if stringElement > list2[i]:
                Numfinity.sumDecimalNumfinitySameSign(
                    convertedDecimal, convertedIntegral, list1, list2, i)

            # If the element's number of list1 is smaller
            elif stringElement < list2[i]:
                Numfinity.sumDecimalNumfinitySameSign(
                    convertedDecimal, convertedIntegral, list2, list1, i)

            # If both are equal
            else:
                # If there are no more elements at the left
                if i - 1 == -1:
                    # Add the residual + the value in integral[-1]
                    convertedIntegral[-1] = str(((2 * int(list1[i])) // (
                        10**15)) + int(convertedIntegral[-1]))

                else:
                    # Add the residual to the element at the left
                    convertedDecimal[i - 1] = str(((2 * int(
                        list1[i])) // (10**15)) + int(convertedDecimal[i - 1]))

                # Always sum the values until 15 digits
                convertedDecimal[i] = str(2 * int(
                    list1[i]))[-15:]
