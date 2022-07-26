import numpy as np

# calculates angular distance between two objects using right ascension and declination.

def angular_dist(rasc1, dec1, rasc2, dec2):
    # converts the distance to radians.
    
    r1 = np.radians(rasc1)
    d1 = np.radians(dec1)
    r2 = np.radians(rasc2)
    d2 = np.radians(dec2)
    
    # get's the absolute distance between the objects and calculates the angle.
    
    deltar = np.abs(r1 - r2)
    deltad = np.abs(d1 - d2)
    angle = 2*np.arcsin(np.sqrt(np.sin(deltad/2)**2 + np.cos(d1)*np.cos(d2)*np.sin(deltar/2)**2))

    return np.degrees(angle)
