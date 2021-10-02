# Numfinity

A work in progress of a a module for Python 3 with which you can create dynamically sized numbers; in other words, increase their maximum decimal or digit capacity to whatever is required.

You can create Numfinity objects in two ways, the standard way by specifying the sign, integral and decimal part, or by using a float/double (depending on the language). For now you can only add values with equal sign, either add with another Numfinity object or with a float.

It's planned to support addition, subtraction, multiplication and division of Numfinity objects. When the Python 3 version is finished (or at least functional) I plan to transcribe it to Java.

## How to use and examples

### Python 3:

Download the file "Numfinity.py" and import it using `from Numfinity import Numfinity`.

`x = Numfinity()` creates a Numfinity object equal to 0.0.

`y = Numfinity(True, "100", "0")` creates a Numfinity object equal to -100.0.

`x.changeValueByPart(False, "50", "0")` changes the Numfinity object's value to 50.0.

`y.changeValue(50.0)` changes the Numfinity object's value to 50.0, using a float.

`x == y` compare if both Numfinity objects are equal.

`str(x)` return the string representation of the Numfinity object.

`float(x)` return the float representation of the Numfinity object.

`x + y` return the addition (a new Numfinity object) of two Numfinity object.

`x + 5.0` return the addition (a new Numfinity object) of the Numfinity object plus 5.0.

## Notes

The methods with a "_" at the end of its name are not supposed to be used by the user.
