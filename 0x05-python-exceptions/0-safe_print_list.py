!/usr/bin/python3

from tkinter import W


def safe_print_list(my_list=[], x=0):
    """Print x elememts of the list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to be printed.

    Returns:
        The number of elements printed.
    """
    W = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            w += 1
        except IndexError:
            break
    print("")
    return (w)
