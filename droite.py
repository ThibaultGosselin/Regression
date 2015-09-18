from random import random
import numpy as np

x=10*np.random.random(25)

def linear(x,params=(0,1)):

	return params[1]*x+params[0]+N(0,1)


print linear(x, (3,10))
