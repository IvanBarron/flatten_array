""" main.py """

from typing import Union

def get_flatten_array(array: list[Union[int, list]], result: list) -> None:
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

if __name__ == '__main__':
    """ Main flow """

    result_array: list = []
    lista = [[1,2],11,13,[3,4,[5,[6,7]],8,[9,10]]]

    get_flatten_array(lista, result_array)
    print(result_array)
