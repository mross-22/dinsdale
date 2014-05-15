#!/usr/bin/env python

from __future__ import division
import numpy as np
import numpy.matlib as npm

class Controller:

    def __init__(self, number):
        """ Initialize the controller """
        self.u = npm.zeros((3, 1))
        self.w = np.matrix([]) # To be implemented 
        self.received = 0 # To be implemented
        self.y = npm.zeros((3, 1))
        self.n = number # Node number

    def iterate_state(self):
        """ Update controller state """
        self.u += self.y # Compute new value

    def iterate_optimization(self):
        """ Iteration of the optimization problem """
        # To be implemented
        pass  
