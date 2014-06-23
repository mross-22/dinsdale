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

        # ------------- Put your code here -------------
        #
        self.A = T*np.matrix('0 1; -1 -2')
        self.B = T*np.matrix('0; 1')
        self.H_23 = T*np.matrix('1 0; 2 1')
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update the plant state """

        # ------------- Put your code here -------------
        #
        e_23 = .33  #np.random.rand()
        self.x = self.A*self.x + self.B*self.u + e_23*self.H_23*self.w + self.x
        self.y = self.x
        self.v = self.x
        #
        # ----------------------------------------------
