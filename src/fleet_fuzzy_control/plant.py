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
        self.m = [200, 250, 80]
        self.d = [70, 100, 50]
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update the plant state """

        # ------------- Put your code here -------------
        #
        (x, y, psi, u, v, r) = np.nditer(self.x)

        (u, v, r) = (self.T*(v*r*self.m[1]/self.m[0] - u*self.d[0]/self.m[0] + self.u[0, 0]/self.m[0]) + u,
                     self.T*(-u*r*self.m[0]/self.m[1] - v*self.d[1]/self.m[1]) + v,
                     self.T*(u*v*(self.m[0] - self.m[1])/self.m[2] - r*self.d[2]/self.m[2] + self.u[1, 0]/self.m[2]) + r)
        (x, y, psi) = (self.T*(u*np.cos(psi) - v*np.sin(psi)) + x,
                       self.T*(u*np.sin(psi) + v*np.cos(psi)) + y,
                       self.T*r + psi)

        self.x = np.matrix([[x, y, psi, u, v, r]]).T
        self.v = npm.zeros((2, 1))
        #
        # ----------------------------------------------

    def update_output(self):
        """ Update the plant output """

        # ------------- Put your code here -------------
        #
        self.y = self.x[:3, :]
        #
        # ----------------------------------------------