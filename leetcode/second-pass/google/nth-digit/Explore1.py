import numpy as np
from numpy.ma import log, power as pow
from scipy.special import lambertw as W

def idx(n):
    return W((9*n-1)*log(10)) / (9*pow(10, 1/9.)) / log(10) + 1/9.

vidx = np.vectorize(idx)

print(vidx(np.arange(10, 190)))

