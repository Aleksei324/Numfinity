from Numfinity import Numfinity as nf
import unittest


class TestInfiniteNumber(unittest.TestCase):
    """docstring for TestInfiniteNumber."""

    def testNegativeZero(self):
        """Test InfiniteNumber with zero and if it deletes the '-'."""
        actual = str(nf(True, "0", "0"))
        expected = "0.0"
        self.assertEqual(expected, actual)

    def testChangeValueByParts(self):
        """Testing the change of values."""
        actual = nf(False, "1", "1")
        actual = str(actual.changeValueByParts(True, "321", "123"))
        expected = "-321.123"
        self.assertEqual(expected, actual)

    def testChangeValueByPartsLargeValues(self):
        """Testing the change of values with large values."""
        actual = nf(False, "09876543210987654321", "12345678901234567890")
        actual = str(actual.changeValueByParts(
            True,
            "110100900800700600500400300200100",
            "00100200300400500600700800900100110"))
        expected = (
            "-110100900800700600500400300200100." +
            "00100200300400500600700800900100110")
        self.assertEqual(expected, actual)

    def testChangeValue(self):
        """Testing the other method of change of values."""
        actual = nf(False, "1", "1")
        actual = float(actual.changeValue(-321.123))
        expected = -321.123
        self.assertAlmostEqual(expected, actual)

    def testCompareDiferentObjects(self):
        """Test the comparation of diferent Numfinity objects."""
        object = nf(False, "0", "1")
        otherObject = nf(False, "5", "0")
        actual = object == otherObject
        expected = False
        self.assertAlmostEqual(expected, actual)

    def testCompareEqualObjects(self):
        """Test the comparation of equal Numfinity objects."""
        object = nf(False, "0", "1")
        otherObject = nf(False, "5", "0")
        actual = object.changeValue(5.0) == otherObject
        expected = True
        self.assertAlmostEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
