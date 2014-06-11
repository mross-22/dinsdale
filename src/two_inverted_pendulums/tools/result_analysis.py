#!/usr/bin/env python


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


class ResultAnalysis:
    """ Analyse the logged data after execution """

    def __init__(self, number):
        """ Initialize data to be analyzed """

        self.data = {}
        self.data['y'] = [[] for i in xrange(number)]
        self.data['u'] = [[] for i in xrange(number)]
        self.data['v'] = [[] for i in xrange(number)]
        self.data['w'] = [[] for i in xrange(number)]
        self.data['g'] = [[] for i in xrange(number)]
        self.data['h'] = [[] for i in xrange(number)]

    def analyze(self):
        t = np.arange(0, 10, .1)
        p0 = np.array([x[0:2] for x in self.data['y'][0]])
        p1 = np.array([x[0:2] for x in self.data['y'][1]])
        plt.plot(t, p0[:, 0], label = 'plant 0')
        plt.plot(t, p1[:, 0], label = 'plant 1')
        plt.legend()
        plt.xlabel('t [s]')
        plt.show()
