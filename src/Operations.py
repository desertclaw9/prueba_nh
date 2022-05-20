import numpy as np


def operations(x, y, op):
    """
    Calls the right operation selected by op with values
    :param x: value x
    :param y: value y
    :param op: operation to perform
    :return: None
    """
    # list with available operations
    operations_both = ['sum', 'sub', 'mul', 'div', 'pow']
    operations_single = ['sqrt']

    # if y is None only single operations can be made
    if y is None and op in operations_single:
        print(eval(op + '(x)'))
    elif y is not None and op in operations_both:
        print(eval(op + '(x, y)'))
    else:
        raise NotImplementedError('This operation doesn\'t exist or isn\'t implemented yet!')


def sum(x, y):
    """
    sums x and y
    :param x: value 1
    :param y: value 2
    :return: x + y
    """
    return x + y


def sub(x, y):
    """
    substrates x and y
    :param x: value 1
    :param y: value 2
    :return: x - y
    """
    return x - y


def mul(x, y):
    """
    multiply x and y
    :param x: value 1
    :param y: value 2
    :return: x * y
    """
    return x * y


def div(x, y):
    """
    divide x and y
    :param x: value 1
    :param y: value 2 cant be zero
    :return: x / y
    """
    if y == 0:
        raise ValueError('Divide by zero error')
    return x / y


def pow(x, y):
    """
    raises y to x
    :param x: value 1
    :param y: value 2
    :return: x ^ y
    """
    return np.power(x, y)


def sqrt(x):
    """
    square root of x
    :param x: value 1
    :return: sqrt(x)
    """
    return np.sqrt(x)
