import check50
import math
from re import escape


@check50.check()
def exists():
    """circle.py exists"""
    check50.exists("circle.py")


@check50.check(exists)
def test_integer_radius():
    """Input: 1 → Output: 3.14"""
    check50.run("python3 circle.py") \
        .stdin("1\n", prompt=True) \
        .stdout("3.14", regex=False) \
        .exit(0)


@check50.check(exists)
def test_float_radius():
    """Input: 2.5 → Output: 19.63"""
    check50.run("python3 circle.py") \
        .stdin("2.5\n", prompt=True) \
        .stdout("19.63", regex=False) \
        .exit(0)


@check50.check(exists)
def test_zero_radius():
    """Input: 0 → Output: 0.00"""
    check50.run("python3 circle.py") \
        .stdin("0\n", prompt=True) \
        .stdout("0.00", regex=False) \
        .exit(0)