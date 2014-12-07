#!/usr/bin/env python


from __future__ import division
import numpy as np
import numpy.matlib as npm


class Plant:
    """ Define plant dynamics """

    def __init__(self, number, x0, T):
        """ Initialise the plant """

        self.x = x0             # Plant state
        self.u = np.matrix([])  # Input from controller
        self.w = np.matrix([])  # Influence from other plants
        self.v = x0             # Influence to other plants
        self.y = np.matrix([])  # Output for controller
        self.T = T              # Sampling period
        self.n = number         # Node number

        # ------------- Put your code here -------------
        #
        self.A = T*np.matrix('0 1; 2 3')
        self.B = T*np.matrix('0; 1')
        self.H_13 = T*np.matrix('1 2; 3 4')
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update the plant state """

        # ------------- Put your code here -------------
        #
        e_13 = .4
        self.x = self.A*self.x + self.B*self.u + e_13*self.H_13*self.w + self.x
        self.v = self.x
        #
        # ----------------------------------------------

    def update_output(self):
        """ Update the plant output """

        # ------------- Put your code here -------------
        #
        self.y = self.x
        #
        # ----------------------------------------------