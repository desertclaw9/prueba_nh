import argparse
from Operations import operations


def operate(args):
    """
    main function of calculator that retrieves values and calls Operations module
    :param args: values and operation
    :return: None
    """
    x = args["value1"]
    y = args["value2"]
    op = args["operation"]

    operations(x, y, op)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-x", "--value1", required=True, type=float, help="input value x")
    ap.add_argument("-y", "--value2", type=float, help="input value y")
    ap.add_argument("-o", "--operation", required=True, type=str,
                    help="Operation to perform, available options are:\n"
                         "  sum: x + y,\n"
                         "  sub: x - y,\n"
                         "  mul: x * y,\n"
                         "  div: x / y,\n"
                         "  pow: x ^ y\n"
                         "  and sqrt: sqrt(x)"
                    )
    operate(vars(ap.parse_args()))
