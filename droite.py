from random import random
import numpy as np

x=10*np.random.random(25)

def linear(x,params=(0,1)):

	return params[1]*x+params[0]+5*np.random.normal(size=len(x)) """droite+bruit distribué de selon une Gaussienne"""


print linear(x, (3,10))
