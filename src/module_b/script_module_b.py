from time import time

import numpy

some_string = "my string"


def module_b_function():
    print(
        "called module b function. Here is a string that's more than 88 characters"
        "creating issues with flake"
    )
    multi_line_string = (
        "here's a very long string, more than 88 characters long, I"
        "wonder if it'll get reformatted"
    )
    print(multi_line_string)
    print(numpy)
    print(f"Time: {time()}")


def module_b_function_too_complex():  # noqa
    if True:
        if True:
            if True:
                if True:
                    print("Hi")
                elif 1 == 2:
                    print("No")
                elif 3 == 4:
                    print("Not yet")
                elif 4 == 5:
                    print("Not yet")
                elif 6 == 7:
                    print("Still not yet")

                if False:
                    if True:
                        print("No")


def complex_function(x):  # noqa
    result = 0
    for i in range(x):
        for j in range(i):
            for k in range(j):
                if i + j + k > x:
                    result += i * j * k
                else:
                    result -= i * j * k
    return result
