import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def coord(file):
    tempfits = fits.open(file)
    data = tempfits[1].data
    coord = np.zeros([len(data),2])
    for i in range(len(data)):
        coord[i][0] = data[i][1]
        coord[i][1] = data[i][2]
    return coord

def galaxy_types(file):
    tempfits = fits.open(file)
    data = tempfits[1].data
    types = []
    for i in range(len(data)):
        types.append(data[i][8].strip())
    return types

def plottest(coords, types):
    colors = plt.get_cmap('Spectral')
    for i in range(len(types)):
        if types[i] == ('SPIRAL GALAXY BARRED'):
            types[i] = 1
        elif types[i] == ('SPIRAL GALAXY'):
            types[i] = 2
        elif types[i] == ('IRREGULAR GALAXY'):
            types[i] = 3
        elif types[i] == ('ELLIPTICAL GALAXY'):
            types[i] = 4
    font = {'family':'monospace','color':'black','size':14}
    ax = plt.axes()
    ax.set_facecolor('white')
    plot = plt.scatter(coords[:, :1], coords[:, 1:2], s=10, lw=0, c=types, alpha=0.6, cmap=colors)
    cb = plt.colorbar(plot, ticks=[1, 2, 3, 4])
    cb.set_ticklabels(['SPIRAL BARRED', 'SPIRAL', 'IRREGULAR', 'ELLIPTICAL'])
    plt.title('Coordenates', fontdict = font)
    plt.xlabel('Right Ascension', fontdict = font)
    plt.ylabel('Declination', fontdict = font)
    plt.show()
