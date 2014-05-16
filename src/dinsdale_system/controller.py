#!/usr/bin/env python

from __future__ import division
import numpy as np
import numpy.matlib as npm

class Controller:

    def __init__(self, number):
        """ Initialize the controller """
        self.u = npm.zeros((2, 1))
        self.w = np.matrix([]) # To be implemented 
        self.received = 0 # To be implemented
        self.y = np.matrix([])
        self.n = number # Node number
        
        # ------------- Put your code here -------------
        # 
        self.ref = [np.matrix("[10; 20]"),
                    np.matrix("[-10 10; -20 -20]"),
                    np.matrix("[-10; 20]")]    
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update controller state """
        
        # ------------- Put your code here -------------
        #
        z_i = self.y[:2, 0]
        z_j = self.y[2:, 0].reshape((self.y[2:, 0].size/2,2)).T
        u = npm.zeros((2, 1))
        for i in xrange(z_j.shape[1]):
            u += z_j[:, i] - z_i - self.ref[self.n][:, i]
        self.u = u
        #
        # ----------------------------------------------

    def iterate_optimization(self):
        """ Iteration of the optimization problem """
        # To be implemented
        pass  
