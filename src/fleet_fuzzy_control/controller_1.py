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
        self.u_max = [200, 100]
        self.k = [.5, 3, 10]
        self.t = 0
        self.k_p = [.2, 20, .5]
        self.m = 2
        self.ref_M = 1.5
        self.R = 5
        self.ref = npm.zeros((2, 1))
        self.o = [[90, 0, 40],
                  [35, 5, 50],
                  [25, -30, 25],
                 ]
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update controller state """

        # ------------- Put your code here -------------
        #

        # Sine wave reference trajectory
        #
        #self.t += self.T
        #(x_ref, y_ref) = self.t, np.sin(self.t/15)*20

        if not self.t:
            self.ref = self.y[:2, :]
            self.q = self.ref
            self.t = 1

        (x, y, psi) = np.nditer(self.y)
        (x_ref, y_ref) = np.nditer(self.ref)
        (x_q, y_q) = 150, 0

        F_a = [self.k_p[0]*(x_ref - x_q), self.k_p[0]*(y_ref - y_q)]
        temp = [0, 0]
        for obs in self.o:
            temp[0] -= (x_ref  - obs[0])*np.exp(-1/(2*obs[2])*((x_ref  - obs[0])**2 + (y_ref  - obs[1])**2))
            temp[1] -= (y_ref  - obs[1])*np.exp(-1/(2*obs[2])*((x_ref  - obs[0])**2 + (y_ref  - obs[1])**2))
        F_r = []
        F_r.append(self.k_p[1]*temp[0])
        F_r.append(self.k_p[1]*temp[1])

        (x_ref, y_ref) = (self.T*self.ref_M*np.tanh(.5*(-F_a[0]*np.exp(-self.k_p[2]*F_r[0]**2) - F_r[0] + self.m*F_r[1])) + x_ref,
                          self.T*self.ref_M*np.tanh(.5*(-F_a[1]*np.exp(-self.k_p[2]*F_r[1]**2) - F_r[1] - self.m*F_r[0])) + y_ref)

        no = np.sqrt((x_ref - x)**2 + (y_ref - y)**2)
        vp = (y_ref - y)*np.cos(psi) - (x_ref - x)*np.sin(psi)
        if no:
            vp /= no

        self.u = np.matrix([[self.u_max[0]*np.tanh(self.k[0]*no)*np.exp(-self.k[1]*vp**2)],
                            [self.u_max[1]*np.tanh(self.k[2]*vp)]])
        self.p = self.y[:2, :]
        self.ref = np.matrix([[x_ref, y_ref]]).T
        #
        # ----------------------------------------------

    def iterate_optimisation(self):
        """ Iteration of the optimisation problem """

        # ------------- Put your code here -------------
        #
        pass
        #
        # ----------------------------------------------
