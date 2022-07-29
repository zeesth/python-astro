import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# loads coordinates from file into array.

def coord(file):
    tempfits = fits.open(file)
    data = tempfits[1].data
    coord = np.zeros([len(data),2])
    
    # circles for each index on the fits.
    
    for i in range(len(data)):
        coord[i][0] = data[i][1]
        coord[i][1] = data[i][2]
        
    return coord

# loads galaxy classification into list.

def galaxy_types(file):
    tempfits = fits.open(file)
    data = tempfits[1].data
    types = []
    
    # circles for each index on the fits.
    
    for i in range(len(data)):
        types.append(data[i][8].strip())
        
    return types

# plots the galaxies coordinates and classification.

def plottest(coords, types):
    
    # assign each classification a number.
    
    for i in range(len(types)):
        if types[i] == ('SPIRAL GALAXY BARRED'):
            types[i] = 1
            
        elif types[i] == ('SPIRAL GALAXY'):
            types[i] = 2
            
        elif types[i] == ('IRREGULAR GALAXY'):
            types[i] = 3
            
        elif types[i] == ('ELLIPTICAL GALAXY'):
            types[i] = 4
    
    # imports colormap and loads classifications numbers and labels accordingly.
    
    colors = plt.get_cmap('Spectral')
    plot = plt.scatter(coords[:, :1], coords[:, 1:2], s=10, lw=0, c=types, alpha=0.6, cmap=colors)    
    cb = plt.colorbar(plot, ticks=[1, 2, 3, 4])
    cb.set_ticklabels(['SPIRAL BARRED', 'SPIRAL', 'IRREGULAR', 'ELLIPTICAL'])
    
    # set title, labels and font for each.
    
    font = {'family':'monospace','color':'black','size':14}
    plt.title('Coordinates', fontdict = font)
    plt.xlabel('Right Ascension', fontdict = font)
    plt.ylabel('Declination', fontdict = font)
    
    plt.show()
