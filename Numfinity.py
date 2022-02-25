class Numfinity:
    """
    <Numfinity: a type of variable that allows to store massive numbers.>
    Copyright (C) 2021  Camilo Franco Moya

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA
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

        self.integralPart = Numfinity.convertNumber_(integral, False)
        self.decimalPart = Numfinity.convertNumber_(decimal, True)

        # If the final value equal to 0.0 (str may have more zeros)
        if float(self) == 0.0:
            # remove the negative sign
            self.negative = False
            # remove extra zeroes
            self.integralPart = ["0"]
            self.decimalPart = ["0"]
        else:
            self.negative = negativeSign

        self.original = float(self)

        return self

    def changeValue(self, number=0.0):
        """
        (float) -> Numfinity
        Change the value to another number.
        Use changeValueByPart for more accuracy.
        Have support for int values.
        """
        number = float(number)
        splitNumber = str(number).split(".")

        self.integralPart = Numfinity.convertNumber_(splitNumber[0], False)
        self.decimalPart = Numfinity.convertNumber_(splitNumber[1], True)

        self.negative = Numfinity.determineSign_(number)
        self.original = number

        return self

    @staticmethod
    def convertNumber_(number, decimalMode):
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
                    converted.append(number[(counter * 15) : (counter * 15) + 15])
            else:
                # count until all the items are added
                for counter in range(int(numItems) + 1):
                    # Get the respective item based on the digits and add it
                    converted.insert(
                        0, number[(counter * -15) - 15 : len(number) - (counter * 15)]
                    )

        return converted

    @staticmethod
    def determineSign_(number):
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

    def is_zero(self):
        """
        (Numfinity) -> bool
        Check if the Numfinity object is equal to 0.0.
        """
        # If there is only one element in each list and the numbers on those elements are equal to 0...
        if (
            len(self.integralPart) + len(self.decimalPart) == 2
            and self.integralPart[0] + self.decimalPart[0] == "00"
        ):
            return True
        else:
            return False

    ### COMPARATORS

    def __eq__(self, other):
        """
        (Numfinity, ?) -> bool
        Compare if 2 objects are equal.
        """
        if isinstance(other, Numfinity) or isinstance(other, float):
            return str(self) == str(other)

        elif isinstance(other, int):
            return str(self) == str(other) + ".0"

        elif isinstance(other, str):
            return str(self) == other

        else:
            return NotImplemented

    def __ne__(self, other):
        """
        (Numfinity, ?) -> bool
        Compare if 2 objects are not equal.
        """
        if self == other:
            return False
        else:
            return True

    def comparator(self, other):
        """
        (Numfinity, Numfinity) -> int
        Compares two Numfinity objects
        """
        if isinstance(other, Numfinity):

            if self.negative == False and other.negative == True:
                return 1

            elif self.negative == True and other.negative == False:
                return -1

            else:

                dif = self - other

                if dif.is_zero():
                    return 0

                # If the diference of both numbers is positive and both numbers are positive,
                # which means the first positive number is greater than the second positive number...
                elif (
                    dif.negative == False
                    and not (self.negative)
                    or dif.negative == True
                    and self.negative
                ):
                    return 1

                # If the diference of both numbers is negative and both numbers are positive
                # which means the first negative number is greater than the second negative number...
                elif (
                    dif.negative == True
                    and not (self.negative)
                    or dif.negative == False
                    and self.negative
                ):
                    return -1

        else:
            return NotImplemented

    def __lt__(self, other):
        """
        (Numfinity, ?) -> bool
        Compare if one object is lesser than the other
        """
        result = self.comparator(other)
        if result == -1:
            return True
        else:
            return False

    def __le__(self, other):
        """
        (Numfinity, ?) -> bool
        Compare if one object is lesser or equal than the other
        """
        result = self.comparator(other)
        if result == -1 or result == 0:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        (Numfinity, ?) -> bool
        Compare if one object is greater than the other
        """
        result = self.comparator(other)
        if result == 1:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        (Numfinity, ?) -> bool
        Compare if one object is greater or equal than the other
        """
        result = self.comparator(other)
        if result == 1 or result == 0:
            return True
        else:
            return False

    ### COMPARATORS

    def __add__(self, other):
        """
        (Numfinity, ?) -> Numfinity
        Sum 2 objects. (WIP)
        """
        if isinstance(other, Numfinity):
            # Make compatible both Numfinity objects
            self.preparingOperation_(other)

            result = self.sumNumfinity_(other)

            # Clean both objects
            self.removeExtraZeros_()
            other.removeExtraZeros_()

            # It could have empty elements so I add zeros to fill those
            result.fillWithZeros_()

            return result

        elif isinstance(other, float) or isinstance(other, int):
            # convert float to Numfinity object.
            newOther = Numfinity()
            newOther.changeValue(other)

            # Make compatible both Numfinity objects
            self.preparingOperation_(newOther)

            result = self.sumNumfinity_(newOther)

            # Clean both objects
            self.removeExtraZeros_()
            newOther.removeExtraZeros_()

            # It could have empty elements so I add zeros to fill those
            result.fillWithZeros_()

            return result

        else:
            return NotImplemented

    def __sub__(self, other):
        """
        (Numfinity, ?) -> Numfinity
        substract 2 objects. (WIP)
        """
        if isinstance(other, Numfinity):
            another = Numfinity(not (other.negative))
            another.integralPart = other.integralPart.copy()
            another.decimalPart = other.decimalPart.copy()
            another.original = other.original

            return self + another

        elif isinstance(other, float) or isinstance(other, int):
            return NotImplemented  # TODO: support for this

        else:
            return NotImplemented

    def __mul__(self, other):
        """
        (Numfinity, ?) -> Numfinity
        multiply 2 objects. (WIP)
        """
        if isinstance(other, Numfinity):
            return NotImplemented  # TODO: support for this

        elif isinstance(other, float) or isinstance(other, int):
            return NotImplemented  # TODO: support for this

        else:
            return NotImplemented

    def __div__(self, other):
        """
        (Numfinity, ?) -> Numfinity
        divide 2 objects. (WIP)
        """
        if isinstance(other, Numfinity):
            return NotImplemented  # TODO: support for this

        elif isinstance(other, float) or isinstance(other, int):
            return NotImplemented  # TODO: support for this

        else:
            return NotImplemented

    def preparingOperation_(self, other):
        """
        (Numfinity, Numfinity) -> none
        Make compatible both Numfinity objects.
        Fix the length of 2 Numfinity objects.
        """
        # If the 2 objects have different length, fix it
        while len(self.integralPart) < len(other.integralPart):
            self.integralPart.insert(0, "000000000000000")
        while len(self.integralPart) > len(other.integralPart):
            other.integralPart.insert(0, "000000000000000")

        while len(self.decimalPart) < len(other.decimalPart):
            self.decimalPart.append("000000000000000")
        while len(self.decimalPart) > len(other.decimalPart):
            other.decimalPart.append("000000000000000")

    def sumNumfinity_(self, other):
        """
        (Numfinity, Numfinity) -> Numfinity
        Sum 2 Numfinity objects
        """
        resultingSign = False
        # A list with both the integral and decimal part
        resultingList = []
        # It have on purpose +1 index to do less operations in the future
        referenceIndex = len(self.integralPart)

        # if positive + positive
        if not (self.negative) and not (other.negative):
            resultingList, referenceIndex = self.sumModule_(other, referenceIndex)

        # if negative + negative
        elif self.negative and other.negative:
            resultingSign = True
            resultingList, referenceIndex = self.sumModule_(other, referenceIndex)

        # if positive + negative
        elif not (self.negative) and not (other.negative):
            # TODO: this - - - - -
            pass

        # if negative + positive
        else:
            resultingSign = True
            # TODO: this - - - - -
            pass

        result = Numfinity()
        result.negative = resultingSign
        result.integralPart = resultingList[:referenceIndex]
        result.decimalPart = resultingList[referenceIndex:]
        result.original = float(result)

        return result

    def sumModule_(self, other, referenceIndex):
        """
        (Numfinity, Numfinity, int) -> List, int
        Create a list with the sum, update the reference index if needed.
        (there is no need for the reference index here when substracting)
        """
        # Mix both lists
        selfList = self.integralPart
        selfList.extend(self.decimalPart)

        # Mix both lists
        otherList = other.integralPart
        otherList.extend(other.decimalPart)

        sum = ""

        # Create a new empty list
        result = []
        # Fill it with zeros
        for count in range(len(selfList)):
            result.append("0")

        # Get the index, starting from the last element
        # (result will be modified, so is better to use selfList)
        for index in range(len(selfList) - 1, -1, -1):

            # sum both elements of each list
            sum = str(int(selfList[index]) + int(otherList[index]))

            # store it (only the last 15 digits)
            result[index] = str(int(result[index]) + int(sum[-15:]))

            # If the sum was bigger than the element capacity
            # and it's the last index
            if index == 0 and len(sum) > 15:
                # store it correctly
                result.insert(0, sum[:-14])
                referenceIndex += 1

            # If the sum was bigger than the element capacity
            elif len(sum) > 15:
                # store it correctly
                result[index - 1] = str(int(result[index - 1]) + int(sum[:-14]))

        return result, referenceIndex

    def fillWithZeros_(self):
        """
        (Numfinity) -> none
        Insert zeros when needed.
        """
        for index in range(len(self.integralPart) - 1):
            if index != 0:
                self.integralPart[index] = (
                    "000000000000000" + self.integralPart[index]
                )[-15:]

        for index in range(len(self.decimalPart) - 1, -1, -1):
            if index != len(self.decimalPart) - 1:
                self.decimalPart[index] = ("000000000000000" + self.decimalPart[index])[
                    -15:
                ]

    def removeExtraZeros_(self):
        """
        (Numfinity) -> none
        Remove innecesary zeros in a Numfinity object.
        """
        for element in self.integralPart:
            if element == "000000000000000":
                self.integralPart.pop(0)
            else:
                break

        for index in range(len(self.decimalPart) - 1, -1, -1):
            if self.decimalPart[index] == "000000000000000":
                self.decimalPart.pop(index)
            else:
                break
