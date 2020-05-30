import numpy as np
import scipy.fftpack as scifft
from data import mirrorborders


def random2D(Nx, Ny, ampmax=1, ampmin=0, dtype=float):
    if isinstance(np.complex, dtype):
        u = np.array(ampmax*(np.random.rand(Nx, Ny) + np.random.rand(Nx, Ny)
                     * (1j))/np.sqrt(2), dtype=np.complex) + ampmin
    else:
        u = np.array(ampmax*np.random.rand(Nx, Ny) + ampmin) + ampmin
    return u


def gaussian1D(X, A=1., mu=0., sigma=.5):
    """One dimentional gaussian function

    Arguments:
        X {numpy nd.array} -- argument of the gaussian

    Keyword Arguments:
        A {float} -- amplitude (default: {1})
        mu {float} -- expected value (default: {0})
        sigma {float} -- variance (default: {0.5})

    Returns:
        numpy nd.array -- the gaussian function
    """
    r = pow((X - mu)/sigma, 2)
    g = A*np.exp(-0.5*r)
    return g


def gaussian2D(X, Y, A=1., mu=(0., 0.), sigma=(.5, .5)):
    """Two dimensional gaussian functions

    Arguments:
        X {numpy nd.array} -- argument x of the gaussian
        Y {numpy nd.array} -- argument y of the gaussian

    Keyword Arguments:
        A {float} -- amplitude (default: {1.})
        mu {tuple} -- expected value (default: {(0., 0.)})
        sigma {tuple} -- variance (default: {(.5, .5)})

    Returns:
        numpy nd.array -- the gaussian function
    """
    rx, ry = np.meshgrid(X, Y)
    x2 = pow((rx - mu[0])/sigma[0], 2)
    y2 = pow((ry - mu[1])/sigma[1], 2)
    g = A*np.exp(-0.5*(x2 + y2))
    return g


def nabla2fft(u, kx, ky):
    """Computes the laplacian of a 2D array

    Arguments:
        u {numpy nd.array} -- Array with data to de derived
        kx {numpy nd.array} -- frequencies for x direction
        ky {numpy nd.array} -- frequencies for y direction

    Returns:
        numpy nd array -- data derived
    """
    u_hatx = scifft.fft2(u)
    u_haty = scifft.fft2(u.T)

    d2u_hatx = -np.power(kx, 2)*u_hatx
    d2u_haty = -np.power(ky, 2)*u_haty

    d2ux = scifft.ifft2(d2u_hatx).real
    d2uy = scifft.ifft2(d2u_haty).real

    d2u = d2ux + d2uy.T

    return d2u


def nabla2cs(u, dx2=0.01, dy2=0.01):
    """Computes the laplacian of u, and apply
    periodic bounday conditions

    Arguments:
        u {numpy nd.array} -- 2D array of floats

    Keyword Arguments:
        dx2 {float} -- squared spacing in x-direction (default: {0.01})
        dy2 {float} -- squared spacing in y-direction (default: {0.01})

    Returns:
        numpy nd.array -- the laplacian
    """
    u_ = u  # add_mirror_borders(u)
    uprev = u[1:-1, 1:-1]  # add_mirror_borders(u)[1:-1, 1:-1]
    d2u = ((u_[2:, 1:-1] - 2*uprev + u_[:-2, 1:-1])/dx2
           + (u_[1:-1, 2:] - 2*uprev + u_[1:-1, :-2])/dy2)
    return mirrorborders(d2u)