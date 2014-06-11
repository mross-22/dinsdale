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
        self.A = T*np.matrix('0 1; 3 4')
        self.B = T*np.matrix('0; 1')
        self.H_31 = T*np.matrix('3 0; 2 1')
        self.H_32 = T*np.matrix('1 5; 4 6')
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update the plant state """

        # ------------- Put your code here -------------
        #
        e_31 = .15  #np.random.rand()
        e_32 = .1  #np.random.rand()
        self.x = self.A*self.x + self.B*self.u + e_31*self.H_31*self.w[:2, :] + e_32*self.H_32*self.w[2:, :] + self.x
        self.y = self.x
        self.v = self.x
        #
        # ----------------------------------------------
