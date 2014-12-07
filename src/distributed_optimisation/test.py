from plant import *
import numpy as np

p = Plant(0, np.matrix('0; 0'), np.matrix('0'), .1)

print p.x
print p.u

p.w = np.matrix('2; 2')

print p.w

p.iterate_state()

print p.x
