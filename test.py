print ('Hello world!')

import numpy as np
r = 5
def f(r):
    cir = 2*np.pi * r
    print ('circumrance =',cir)
def g(r):
    area = np.pi* np.power(r,2)
    print ('area =',area)

f(r)
g(r)
