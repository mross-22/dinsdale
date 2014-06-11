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
        self.A = np.matrix([[1, T],
                            [T, 1]])
        self.B = np.matrix([[0, T]]).T
        self.H_this = np.matrix([[0, 0],
                                 [-T, 0]])
        self.H_other = np.matrix([[0, 0],
                                  [T, 0]])
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update the plant state """

        # ------------- Put your code here -------------
        #
        e = np.random.rand()
        self.x = self.A*self.x + self.B*self.u + self.H_this*self.x + self.H_other*self.w
        self.y = self.x
        self.v = self.x
        #
        # ----------------------------------------------
