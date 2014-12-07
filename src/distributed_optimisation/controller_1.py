#!/usr/bin/env python


from __future__ import division
import numpy as np
import numpy.matlib as npm
import numpy.linalg as npl
from cvxopt import matrix, solvers


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
        solvers.options['show_progress'] = False

        Ts = .5
        self.A = np.matrix([[1, Ts], [0, 1]])
        self.B = np.matrix([[Ts**2/2.0], [Ts]])

        self.Qx = np.matrix('.1 0; 0 .1')
        self.Px = np.matrix('4 0; 0 4')
        self.Ru = .4

        self.Q = np.matrix('.01 0; 0 .01')

        self.P = np.matrix('-.3898 -.3836; .2703 .9763')

        cx = 5

        self.bxlow = -cx
        self.bxup = cx

        self.buup = 20

        self.ALPHAconst = 2.0
        #
        # ----------------------------------------------

    def iterate_state(self):
        """ Update controller state """

        self.finished = False

        # ------------- Put your code here -------------
        #
        self.Iter = 0
        self.LAM = .1
        
        self.tau = 1

        self.f = np.matrix([[np.sin(self.y[1,0]), 0]]).T
        self.v = np.matrix([[0, self.y[2,0]]]).T

        self.Ju = self.B
        self.Jx = self.A*self.y[:2,0] + self.f + self.v

        self.Zu = self.Px*self.B
        self.Zx = self.Px*self.Jx

        self.Ku = self.P*self.B
        self.Kx = self.P*self.Jx

        self.c1 = npl.norm(self.Qx*self.y[:2,0], np.inf)
        self.c2 = npl.norm(self.P*self.y[:2,0], np.inf) - npl.norm(self.Q*self.y[:2,0], np.inf)

        self.u = np.matrix([[0]])
        self.p = np.matrix([[0]])
        #
        # ----------------------------------------------

    def iterate_optimisation(self):
        """ Iteration of the optimisation problem """

        # ------------- Put your code here -------------
        #
        if self.Iter:
            self.LAM += self.ALPHA*(self.tau + self.s[0,0])
            if ((abs(self.tau + self.s[0,0]) <= 1E-5 and abs(self.LAM*(self.tau + self.s[0,0])) < 1E-5) or self.Iter >= 100):
                self.finished = True
                return

        self.Iter += 1
        self.ALPHA = self.ALPHAconst/np.sqrt(self.Iter)

        fL = np.matrix([[1, 1, 0, self.LAM]]).T

        AL1 = np.matrix([[0, 0, 1, 0],
                         [0, 0, -1, 0],
                         [-1, 0, 0, 0],
                         [0, -1, 0, 0],
                         [0, 0, 0, 1],
                         [0, 0, 0, -1],
                         [0, 0, self.Ju[0,0], 0],
                         [0, 0, -self.Ju[0,0], 0],
                         [0, 0, self.Ju[1,0], 0],
                         [0, 0, -self.Ju[1,0], 0],
                         [0, 0, self.Ku[0,0], -1],
                         [0, 0, -self.Ku[0,0], -1],
                         [0, 0, self.Ku[1,0], -1],
                         [0, 0, -self.Ku[1,0], -1],
                         [-1, 0, self.Zu[0,0], 0],
                         [-1, 0, -self.Zu[0,0], 0],
                         [-1, 0, self.Zu[1,0], 0],
                         [-1, 0, -self.Zu[1,0], 0],
                         [0, -1, self.Ru, 0],
                         [0, -1, -self.Ru, 0]])

        bL1 = np.matrix([[self.buup],
                         [self.buup],
                         [0],
                         [0],
                         [1000],
                         [1000],
                         [self.bxup - self.Jx[0,0]],
                         [self.Jx[0,0] - self.bxlow],
                         [self.bxup - self.Jx[1,0]],
                         [self.Jx[1,0] - self.bxlow],
                         [-self.Kx[0,0] + self.c2],
                         [self.Kx[0,0] + self.c2],
                         [-self.Kx[1,0] + self.c2],
                         [self.Kx[1,0] + self.c2],
                         [-self.c1 - self.Zx[0,0]],
                         [-self.c1 + self.Zx[0,0]],
                         [-self.c1 - self.Zx[1,0]],
                         [-self.c1 + self.Zx[1,0]],
                         [0],
                         [0]])

        AL_c = matrix(AL1)
        bL_c = matrix(bL1)
        fL_c = matrix(fL)

        sol  = solvers.lp(fL_c, AL_c, bL_c)
        Opt = sol['x']

        self.u = np.matrix([[Opt[2,0]]])
        self.tau = Opt[3,0]

        self.r = np.matrix([[self.tau]])
        #
        # ----------------------------------------------
