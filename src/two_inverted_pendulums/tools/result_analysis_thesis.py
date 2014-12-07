#!/usr/bin/env python


from __future__ import division
import sys
sys.dont_write_bytecode = True
import numpy as np
from thesis import *
import matplotlib.pyplot as plt


class ResultAnalysis:
    """ Analyse the logged data after execution """

    def __init__(self, number):
        """ Initialize data to be analysed """

        self.data = {}
        self.data['y'] = [[] for i in xrange(number)]
        self.data['u'] = [[] for i in xrange(number)]
        self.data['v'] = [[] for i in xrange(number)]
        self.data['w'] = [[] for i in xrange(number)]
        self.data['g'] = [[] for i in xrange(number)]
        self.data['h'] = [[] for i in xrange(number)]

    def analyse(self):
        """ Do something with the data """
        
        # ------------- Put your code here -------------
        #
        t = np.arange(0, 10, .01)
        p0 = np.array([x[0:2] for x in self.data['y'][0]])
        p1 = np.array([x[0:2] for x in self.data['y'][1]])

        fig, ax = newfig(.7)
        ax.plot(t, p0[:, 0], label = r'plant 0')
        ax.plot(t, p1[:, 0], label = r'plant 1')
        ax.legend()
        ax.set_xlabel(r'$t\, [\mathrm{s}]$')
        ax.set_ylabel(r'$[x_i]_1\, [\mathrm{rad}]$')
        savefig('pendulums_x1')

        fig, ax = newfig(.7)
        ax.plot(t, p0[:, 1], label = r'plant 0')
        ax.plot(t, p1[:, 1], label = r'plant 1')
        ax.legend()
        ax.set_xlabel(r'$t\, [\mathrm{s}]$')
        ax.set_ylabel(r'$[x_i]_2\, \left[\frac{\mathrm{rad}}{\mathrm{s}}\right]$')
        savefig('pendulums_x2')
        #
        # ----------------------------------------------