""" main.py """

from typing import Union

def get_flatten_array(array: list[Union[int, list]], result: list):
    """ Flatten array 2D Array to 1D Array

    Parameters
    ----------
    array : list of integers and list
        array to be flatten
    result: refefence to a list
        list which will be the result of flatten array

    return
    ------
    None

    """

    for item in array:
        if type(item) is list:
            get_flatten_array(item, result)
        else:
            result.append(item)


def flatten_array(array: list[Union[int, list]]) -> list[int]:
    """ Proxy function to invoke get_flatten_array

    Parameters
    ----------
    array : list of integers and list
        array to be flatten

    return
    ------
    list: lit of integers
        list flatten in 1D

    """
    result: list = []
    if not type(array) is list:
        raise ValueError("Array argumnet must be a list")
        
    get_flatten_array(array, result)
    
    return result

