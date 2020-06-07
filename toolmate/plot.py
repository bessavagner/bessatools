import matplotlib.pyplot as plt
import numpy as np
import toolmate.data as data


def getscale(u, xrange=(-1, 1)):
    """Creates a list of length len(u) of equally spaced
    floats from xrange[0] to xrange[1]. It works exactly as
    ```
        Nx = len(u)
        xscale = np.linspace(xrange[0], xrange[1], Nx)
    ```

    Arguments:
        u {Sequence} -- a sequence of shape (len(u),)

    Keyword Arguments:
        xrange {tuple} -- xtremes of the scale (default: {(-1, 1)})

    Raises:
        ValueError: sequence must be 1D and have the same type
    Returns:
        ndarray -- scale
    """
    try:
        _shape = data.shape(u)
    except RecursionError as err:
        print("Inhomogenous data: ", err)
    if len(_shape) != 1:
        raise ValueError("Can't create 1D scale from array"
                         f" of shape {_shape}")
    checkhomogeneity = data.allsametype(u)
    if not checkhomogeneity:
        raise ValueError(
            f"Inhomogenous list: one element has type {checkhomogeneity}")
    Nx = len(u)
    xscale = np.linspace(xrange[0], xrange[1], Nx)
    return xscale


def getgrid(u, xrange=(-1, 1), yrange=(-1, 1)):
    """Generates a mesh grid based on a 2D array

    Arguments:
        u {2D array} -- The 2D matrix to be based on

    Keyword Arguments:
        xrange {tuple} -- range in x direction (default: {(-1, 1)})
        yrange {tuple} -- range in y direction (default: {(-1, 1)})

    Returns:
        ndarray -- numpy array corresponding to a meshgrid
    """
    u_ = np.array(u)
    xscale = getscale(u_[0, :], xrange=xrange)
    yscale = getscale(u_[:, 0], xrange=yrange)
    return np.meshgrid(xscale, yscale)


def plotxy(Y, xrange=(-1, 1), size=(6, 6),
           scaled=True, figname=None, show=True, **kwargs):
    plt.ioff()
    fig = plt.figure(figsize=size)
    X = getscale(Y, xrange=xrange)
    plt.plot(X, Y, **kwargs)
    if scaled:
        plt.axis('scaled')
    if isinstance(figname, str):
        plt.savefig(figname)
    if show:
        plt.show()
    fig.clear()
    plt.close(fig)


def plotf(func, xrange=(-1, 1), dx=0.1, size=(6, 6),
          scaled=True, figname=None, show=True, **kwargs):
    plt.ioff()
    fig = plt.figure(figsize=size)
    X = np.arange(*xrange, dx)
    plt.plot(X, func(X), **kwargs)
    if scaled:
        plt.axis('scaled')
    if isinstance(figname, str):
        plt.savefig(figname)
    if show:
        plt.show()
    fig.clear()
    plt.close(fig)


def plotsurface(u, xrange=(-1, 1), yrange=(-1, 1),
                size=(6, 6), cbar=True, scaled=True,
                figname=None, show=True, level=50, **kwargs):

    plt.ioff()
    rx, ry = getgrid(u, xrange=xrange, yrange=yrange)
    fig = plt.figure(figsize=size)
    plt.contourf(rx, ry, u, level, **kwargs)
    if scaled:
        plt.axis('scaled')
    if cbar:
        plt.colorbar()
    if isinstance(figname, str):
        plt.savefig(figname)
    if show:
        plt.show()
    fig.clear()
    plt.close(fig)
