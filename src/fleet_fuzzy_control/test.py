#!/usr/bin/env python

import sys
sys.dont_write_bytecode = True
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt

import plant
import controller
import controller_1


def two_boats_test():
    T_f = 150
    T_s = .01
    t = np.arange(0, T_f, T_s)
    c = controller_1.Controller(0, T_s)
    c.q = np.matrix('150; 0')
    p = plant.Plant(0,
                    npm.matrix([[0, -30, 0, 1, 0, 0]]).T,
                    np.matrix([[0, 0]]).T,
                    T_s,
                    )
    x = np.zeros((6, t.size))
    x_ref = np.zeros((2, t.size))
    c_1 = controller.Controller(0, T_s)
    p_1 = plant.Plant(0,
                      npm.matrix([[50, 60, 0, 1, 0, 0]]).T,
                      np.matrix([[0, 0]]).T,
                      T_s,
                     )
    x_1 = np.zeros((6, t.size))
    x_1_ref = np.zeros((2, t.size))

    for i, time in enumerate(t):
        x[:, i] = np.reshape(p.x.T, 6)
        p.iterate_state()
        c.y = p.y
        c.iterate_state()
        x_ref[:, i] = np.reshape(c.ref.T, 2)
        p.u = c.u
        c_1.q = c.p
        x_1[:, i] = np.reshape(p_1.x.T, 6)
        p_1.iterate_state()
        c_1.y = p_1.y
        c_1.iterate_state()
        x_1_ref[:, i] = np.reshape(c_1.ref.T, 2)
        p_1.u = c_1.u

    x[:, -1] = np.reshape(p.x.T, 6)
    x_1[:, -1] = np.reshape(p_1.x.T, 6)
    plt.plot(x[0, :], x[1, :], label='boat')
    plt.plot(x_ref[0, :], x_ref[1, :], label='reference')
    plt.plot(x_1[0, :], x_1[1, :], label='boat 1')
    plt.plot(x_1_ref[0, :], x_1_ref[1, :], label='reference 1')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def potential_fields_test():
    T_f = 150
    T_s = .01
    t = np.arange(0, T_f, T_s)
    c = controller_1.Controller(0, T_s)
    c.q = np.matrix('150; 0')
    p = plant.Plant(0,
                    npm.matrix([[0, 60, 0, 1, 0, 0]]).T,
                    np.matrix([[0, 0]]).T,
                    T_s,
                    )
    x = np.zeros((6, t.size))
    x_ref = np.zeros((2, t.size))
    for i, time in enumerate(t):
        x[:, i] = np.reshape(p.x.T, 6)
        x_ref[:, i] = np.reshape(c.ref.T, 2)
        p.iterate_state()
        c.y = p.y
        c.iterate_state()
        p.u = c.u
    x[:, -1] = np.reshape(p.x.T, 6)
    plt.plot(x[0, :], x[1, :], label='boat')
    plt.plot(x_ref[0, :], x_ref[1, :], label='reference')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def controlled_plant_test():
    T_f = 150
    T_s = .01
    t = np.arange(0, T_f, T_s)
    c = controller.Controller(0, T_s)
    p = plant.Plant(0,
                    npm.matrix([[15, 30, np.pi, 5, 0, 0]]).T,
                    np.matrix([[0, 0]]).T,
                    T_s,
                    )
    x = np.zeros((6, t.size))
    for i, time in enumerate(t):
        x[:, i] = np.reshape(p.x.T, 6)
        p.iterate_state()
        c.y = p.y
        c.iterate_state()
        p.u = c.u
    x[:, -1] = np.reshape(p.x.T, 6)
    plt.plot(x[0, :], x[1, :], label='boat')
    plt.plot(t, np.sin(t/15)*20, label='reference')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def controller_test():
    c = controller.Controller(0, .01)
    c.y = np.matrix([[0, 0, 0]]).T
    c.iterate_state()
    print c.u

def plant_test():
    T_f = 80
    T_s = .01
    t = np.arange(0, T_f, T_s)
    p = plant.Plant(0,
                    npm.matrix([[0, 0, np.pi/4, 0, 0, 0]]).T,
                    np.matrix([[25, -5]]).T,
                    T_s,
                    )
    x = np.zeros((6, t.size))
    for i, time in enumerate(t):
        x[:, i] = np.reshape(p.x.T, 6)
        p.iterate_state()
    x[:, -1] = np.reshape(p.x.T, 6)
    plt.plot(x[0, :], x[1, :], label='boat')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def main():
    #plant_test()
    #controller_test()
    #controlled_plant_test()
    #potential_fields_test()
    two_boats_test()

if __name__ == '__main__':
    main()
