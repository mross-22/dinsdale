#!/usr/bin/env python

from __future__ import division
import numpy as np
import numpy.matlib as npm

class Plant:

    def __init__(self, number, x0, u0, T):
        """ Initialize the plant """
        self.x = x0
        self.u = u0
        self.w = np.matrix([]) # Influence from other plants
        self.v = x0 # Influence to other plants
        self.y = np.matrix([])
        self.T = T # Sampling period
        self.n = number # Node number

    def iterate_state(self):
        """ Update the plant state """
        self.x = self.x + self.u
        self.y = self.w
        self.v = self.x