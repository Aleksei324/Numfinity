from Numfinity import Numfinity as nf
import unittest


class TestNumfinity(unittest.TestCase):
    """Test the Python 3 version of Numfinity."""

    def testNegativeZero(self):
        """Test Numfinity with zero and if it deletes the '-'."""
        actual = str(nf(True, "0", "0"))
        expected = "0.0"
        self.assertEqual(expected, actual)

    def testEmptyStrings(self):
        """Test Numfinity with empty strings."""
        actual = str(nf(True, "", ""))
        expected = "0.0"
        self.assertEqual(expected, actual)

    def testNoParameters(self):
        """Test Numfinity with no parameters."""
        actual = str(nf())
        expected = "0.0"
        self.assertEqual(expected, actual)

    def testSomeParameters(self):
        """Test Numfinity with some parameters."""
        actual = str(nf(True, "1"))
        expected = "-1.0"
        self.assertEqual(expected, actual)

    def testInvalidParameters(self):
        """Test Numfinity with invalid parameters."""
        actual = False

        try:
            nf(True, "1.1", "1")
        except AssertionError:
            actual = True

        expected = True
        self.assertEqual(expected, actual)

    def testInvalidTypeParameters(self):
        """Test Numfinity with invalid type parameters."""
        actual = False

        try:
            nf(True, 1, "1")
        except Exception:
            actual = True

        expected = True
        self.assertEqual(expected, actual)

    def testChangeValueByPart(self):
        """Testing the change of values."""
        actual = nf(False, "1", "1")
        actual = str(actual.changeValueByPart(True, "321", "123"))
        expected = "-321.123"
        self.assertEqual(expected, actual)

    def testChangeValueByPartLargeValues(self):
        """Testing the change of values with large values."""
        actual = nf(False, "09876543210987654321", "12345678901234567890")
        actual = str(actual.changeValueByPart(
            True,
            "110100900800700600500400300200100",
            "00100200300400500600700800900100110"))
        expected = (
            "-110100900800700600500400300200100." +
            "00100200300400500600700800900100110")
        self.assertEqual(expected, actual)

    def testChangeValue(self):
        """Testing the other method of change of values."""
        actual = nf()
        actual = float(actual.changeValue(-321.123))
        expected = -321.123
        self.assertEqual(expected, actual)

    def testChangeValueLargeValues(self):
        """Testing the other method of change of values with large values."""
        object = nf()
        actual = float(object.changeValue(6543210987654321.1234567890123456))
        expected = 6543210987654321.1234567890123456
        self.assertAlmostEqual(expected, actual)

    def testChangeValueWithInt(self):
        """Testing the other method of change of values with int."""
        actual = nf()
        actual = float(actual.changeValue(321))
        expected = 321.0
        self.assertEqual(expected, actual)

    def testCompareDiferentObjects(self):
        """Test the comparation of diferent Numfinity objects."""
        object = nf(False, "0", "1")
        otherObject = nf(False, "5", "0")
        actual = object == otherObject
        expected = False
        self.assertEqual(expected, actual)

    def testCompareEqualObjects(self):
        """Test the comparation of equal Numfinity objects."""
        object = nf()
        otherObject = nf(False, "5", "0")
        actual = object.changeValue(5.0) == otherObject
        expected = True
        self.assertEqual(expected, actual)

    def testOriginalAtribute(self):
        """Test if the original atribute is saved correctly."""
        object = nf(False, "54321", "12345")
        actual = object.original
        expected = 54321.12345
        self.assertEqual(expected, actual)

    def testSumZero(self):
        """Test if 0 + 0 is done correctly."""
        object = nf()
        otherObject = nf()
        actual = str(object + otherObject)
        expected = "0.0"
        self.assertEqual(expected, actual)

    def testSumNumfinity(self):
        """Test if the sum of 2 objects is done correctly."""
        object = nf(False, "54321", "12345")
        otherObject = nf(False, "12345", "54321")
        actual = str(object + otherObject)
        expected = "66666.66666"
        self.assertEqual(expected, actual)

    def testSumNegativeNumfinity(self):
        """Test if the sum of 2 negative objects is done correctly."""
        object = nf(True, "54321", "12345")
        otherObject = nf(True, "12345", "54321")
        actual = str(object + otherObject)
        expected = "-66666.66666"
        self.assertEqual(expected, actual)

    def testSumNumfinityLargeValues(self):
        """Test if the sum of 2 large objects is done correctly."""
        object = nf(False, "543210987654321", "123456789012345")
        otherObject = nf(False, "511111011111111", "1111111101111111")
        actual = str(object + otherObject)
        expected = "1054321998765432.2345678991234561"
        self.assertEqual(expected, actual)

    def testSumFloat(self):
        """Test if the sum of 2 objects is done correctly."""
        object = nf(False, "54321", "12345")
        actual = str(object + 12345.54321)
        expected = "66666.66666"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
