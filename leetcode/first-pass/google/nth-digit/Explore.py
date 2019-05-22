from scipy.optimize import broyden1
import numpy as np
import matplotlib.pyplot as plt

def f(k):
    return lambda n: pow(10, n) * (n - 1/9.) + 1/9. - k

def solve(k, n0):
    return broyden1(f(k), n0)

def solve_vec(ks, n0):
    return np.vectorize(lambda k: solve(k, n0))(ks)

#ks = np.arange(10, 190)
#n0 = 2
ks = np.arange(191, 2700)
n0 = 3
ns = solve_vec(ks, n0)
nsd, _ = np.modf(ns)
print(len(ns))
print(nsd)
plt.plot(nsd)
plt.show()




