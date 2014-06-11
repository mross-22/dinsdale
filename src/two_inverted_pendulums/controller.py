#!/usr/bin/env python

from __future__ import division
import numpy as np
import numpy.matlib as npm

class Controller:

    def __init__(self, number):
        """ Initialize the controller """
        self.u = npm.zeros((2, 1))
        self.g = np.matrix([]) # To be implemented
        self.h = np.matrix([]) # To be implemented
        self.received = 0 # To be implemented
        self.y = np.matrix([])
        self.n = number # Node number

        # ------------- Put your code here -------------
        #
        self.K = np.matrix('-3.008 -3.0032')
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update controller state """

        # ------------- Put your code here -------------
        #
        self.u = self.K*self.y
        #
        # ----------------------------------------------

    def iterate_optimization(self):
        """ Iteration of the optimization problem """
        # To be implemented
        pass
