#!/usr/bin/env python

from __future__ import division
import numpy as np
import numpy.matlib as npm

class PlantsTopology:
    """ Topology of plant interactions """
    
    def __init__(self, A):
        """ Initialize the dynamic topology """
        
        self.A = A # Adjacency matrix
        self.nodes = self.A.shape[0] # Total number of nodes
        self.w = [np.array([], dtype = np.float32) for i in xrange(self.nodes)] # Data from plants
        self.communication = [[] for i in xrange(self.nodes)] # Communication graph
    
    def update_topology(self):
        """ Intended to be empty """        
        pass
    

class StaticPlantsTopology(PlantsTopology):
    """ Static interaction topology """
    
    def __init__(self, A):
        """ Extend the initialization """
        
        PlantsTopology.__init__(self, A)
        
        # Communication graph computation
        for node in xrange(self.nodes):
            for neighbour in xrange(self.nodes):
                if self.A[node, neighbour] != 0:
                    self.communication[node].append(neighbour)
                    

class DynamicPlantsTopology(PlantsTopology):
    """ Dynamically changing imteraction topology """
        
    def update_topology(self):
        """ Update plants communication topology """
        
        # ------------- Put your code here -------------
        #
        pass
        #
        # ----------------------------------------------
