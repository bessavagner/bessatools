#  DATA TOOLS
#  ---

import numpy as np
import os
from .files import mkdir

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
    mkdir(dirname, silent=True)
    filepath = dirname + "/" + filebasename
    if isinstance(fileindex, type(None)):
        filepath + '.csv'
    else:
        filepath += f"{fileindex:0{leadingzeros}d}.csv"
    np.savetxt(filepath, data, delimiter=',', **kwargs)

    return filepath