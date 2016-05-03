import math

def foo():
    return math.exp(1000)

try:
    foo()
except(ArithmeticError, AssertionError, ZeroDivisionError) as e:
    if e.__class__.__name__ == "OverflowError":
        print("ArithmeticError")
    elif e.__class__.__name__ == "FloatingPointError":
        print("ArithmeticError")
    else:
        print(e.__class__.__name__)