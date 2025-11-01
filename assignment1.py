import numpy as np

def find_period(L0,L1):
    g=9.81 # in m/s**2
    if not (L1>L0>0):
        return None, None
    
    for L in range(L0, L1 +1):
        T=2*np.pi*np.sqrt(L/g)
        print("When L = %5.1f m, T = %4.1f s" % (L,T))
    T0=2*np.pi*np.sqrt(L0/g)
    T1=2*np.pi*np.sqrt(L1/g)
    return T0,T1
