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
        Ts = .7
        self.A = np.matrix([[1, Ts], [0, 1]])
        self.B = np.matrix([[Ts**2/2.0], [Ts]])
        #
        # ----------------------------------------------


    def iterate_state(self):
        """ Update the plant state """

        # ------------- Put your code here -------------
        #
        ff = np.matrix([[np.sin(self.x[1,0]), 0]]).T
        vv = np.matrix([[0, self.w[0,0]**2]]).T
        self.x = self.A*self.x + self.B*self.u + vv + ff
        self.v = self.x[0,0]
        #
        # ----------------------------------------------


    def update_output(self):
        """ Update the plant output """

        # ------------- Put your code here -------------
        #
        self.y = np.bmat([[self.x], [self.w[0]]])
        #
        # ----------------------------------------------
