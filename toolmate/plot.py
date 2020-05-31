import matplotlib.pyplot as plt
import numpy as np

def getgrid(u, xrange=(-1, 1), yrange=(-1, 1)):
    Nx = len(u[0, :])
    Ny = len(u[:, 0])
    xscale = np.linspace(xrange[0], xrange[1], Nx)
    yscale = np.linspace(yrange[0], yrange[1], Ny)

    return np.meshgrid(xscale, yscale)


def plotsurface(u, xrange=(-1, 1), yrange=(-1, 1),
                size=(6, 6), cbar=True, scaled=True,
                figname=None, show=False, level=50, **kwargs):

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