#  DATA TOOLS
#  ---

import os
import random
import numpy as np
import toolmate.files as files
from collections.abc import Sequence


def allsametype(seq):
    """Tests if seq's elements are all the same type

    Arguments:
        seq {sequence} -- nay sequence to be tested

    Returns:
        type(seq)/False -- if all has the same type/ if any has different type
    """
    iseq = iter(seq)
    first_type = type(next(iseq))
    return first_type if not all( (type(x) is first_type) for x in iseq ) else True


def isndarray(arr):
    if type(arr).__name__ != ndarray():
        return False
    return True


def ndarray():
    return type(np.array([]))


def shape(lst, _shape=()):
    """
    Returns the shape of nested lists similarly to numpy's shape.
    Acknowledgment: https://stackoverflow.com/a/51961249/13599189

    Arguments:
        lst: the nested list
        shape: the shape up to the current recursion depth (default: ())
    Returns:
        the shape including the current depth
        (finally this will be the full depth)
    """
    if not isinstance(lst, (Sequence, ndarray())):
        return _shape
    if isinstance(lst[0], Sequence):
        l = len(lst[0])
        if not all(len(item) == l for item in lst):
            msg = 'not all lists have the same length'
            raise ValueError(msg)
    _shape += (len(lst), )
    _shape = shape(lst[0], _shape)
    return _shape


def mirrorborders(data_):
    """Expand a 2D numpy array by mirroning the borders

    Arguments:
        data_ {numpy nd.array} -- float data in 2D shape

    Returns:
        numpy nd.array -- 2D array expanded
    """
    Nx = len(data_[0, :])
    Ny = len(data_[:, 0])
    data_expanded = np.zeros((Ny + 2, Nx + 2), dtype=np.complex_)
    data_expanded[1:-1, 1:-1] = data_
    data_expanded[:, 0] = np.append(
        np.append(data_[-1, -1], data_[:, -1]), data_[0, -1])
    data_expanded[:, -1] = np.append(
        np.append(data_[-1, 0], data_[:, 0]), data_[0, 0])
    data_expanded[0, 1: -1] = data_[-1, :]
    data_expanded[-1, 1:-1] = data_[0, :]
    return data_expanded


def savecsv(data, filebasename='file', dirname=os.getcwd(),
            fileindex=None, leadingzeros=1, delimiter=',', **kwargs):
    files.mkdir(dirname, silent=True)
    filepath = dirname + "/" + filebasename
    if isinstance(fileindex, type(None)):
        filepath + '.csv'
    else:
        filepath += f"{fileindex:0{leadingzeros}d}.csv"
    np.savetxt(filepath, data, delimiter=',', **kwargs)

    return filepath

def sortedsample(base, n=2):
    """Creates an ordered sorted list based on a given list

    Arguments:
        base {list} -- list base to sample

    Keyword Arguments:
        n {int} -- number of elements to sample (default: {2})

    Returns:
        list -- orderd sorted list
    """
    sample_ = random.sample(list(enumerate(base)), n)
    sortedsample_ = sorted(sample_, key=lambda x:x[0])
    return [item[1] for item in sortedsample_]

