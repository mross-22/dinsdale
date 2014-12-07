#!/usr/bin/env python


from __future__ import division
import numpy as np
import numpy.matlib as npm


class Controller:
    """ Define control law """

    def __init__(self, number, T):
        """ Initialise the controller """

        self.u = np.matrix([])  # Output for plant
        self.p = np.matrix([])  # Output for other controllers
        self.q = np.matrix([])  # Input from other controllers
        self.y = np.matrix([])  # Input from plant
        self.r = np.matrix([])  # Output for iterative communication
        self.s = np.matrix([])  # Input from iterative communication
        self.n = number         # Node number
        self.T = T              # Sampling period
        self.finished = False   # Is optimisation finished

        # ------------- Put your code here -------------
        #
        self.K = np.matrix('-0.67 -1.48')
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update controller state """

        # ------------- Put your code here -------------
        #
        self.u = self.K*self.y
        #
        # ----------------------------------------------

    def iterate_optimisation(self):
        """ Iteration of the optimisation problem """

        # ------------- Put your code here -------------
        #
        pass
        #
        # ----------------------------------------------
