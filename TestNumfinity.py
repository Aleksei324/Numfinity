import Numfinity as nf
import unittest


class TestInfiniteNumber(unittest.TestCase):
    """docstring for TestInfiniteNumber."""

    def testZero(self):
        """Test InfiniteNumber with zero"""
        actual = str(nf.changeValue(0.0))
        expected = "0.0"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)

    var = nf(0.0)

    print(var.changeValue(0.1))
    print(var.changeValue(1.0))
    print(var.changeValue(100.001))

    print(var.changeValue(-2432902008176640000))
    print(var.changeValue(543210987654321.123456789012345))

    print(var.changeValueByParts(True, "00000", "00000"))
    print(var.changeValueByParts(
        True, "243290200817664000024329020081766400002432902008176640000",
        "243290200817664000024329020081766400002432902008176640000"))

    print(float(var))
