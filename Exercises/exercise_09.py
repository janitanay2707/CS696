import sys
import numpy
import pandas
import time
import math

def outer_def(my_function):

    def inner_def():
        t0 = time.time()
        r0 = time.process_time()
        result = my_function()
        t1 = time.time()
        r1 = time.process_time()
        print("Time difference for '{}' is {} seconds".format(my_function._name_, t1 - t0))
        print("Process time taken for '{}' is {} seconds".format(my_function._name_, r1 - r0))
        print("Size of '{}'is {}".format(my_function._name_,sys.getsizeof(result)))
        return result

    return inner_def


def for_loop():
    empty = []
    for x in range(1,1000000):
        empty.append(x)
    return empty

def list_comp():
    return [x for x in range(1,1000000)]

def numpy_list():
    return numpy.arange(1,1000000)


def pandas_list():
    return pandas.Series(range(1,1000000))


def generator_list():
    return (x for x in range(1,1000000))


def for_loop_log():
    empty = []
    for x in range(1,1000000):
        empty.append(math.log10(x))
    return empty


def list_comp_log():
    return [math.log10(x) for x in range(1,1000000)]


def numpy_list_log():
    x = numpy.arange(1,1000000)
    return numpy.log10(x)


def pandas_list_log():
    x = pandas.Series(range(1,1000000))
    return numpy.log10(x)


def generator_list_log():
    return (math.log10(x) for x in range(1,1000000))

