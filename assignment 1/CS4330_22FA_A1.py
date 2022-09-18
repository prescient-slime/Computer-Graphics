# CS 4330
# FALL 2022
# Assignment 1
# Name:
# Buff-id:

import numpy as np
import matplotlib.pyplot as plt


def init_plot():
    plt.axis('equal')
    plt.ylim(-1.5,1.5)
    plt.xlim(-1.5,1.5)
    plt.grid(ls='dashed')
    plt.xlabel("x")
    plt.ylabel("y")


# plots the vector
# p1_, p2_ are points of a vector (p1 is the origin)
# c is color
def plot_vec(p1_,p2_,c):
    plt.quiver(p1_[0], p1_[1], p2_[0], p2_[1], color=[c], units='xy', scale=1)


# plots rotated vector represented by p1_ and p2_
# p1_ is the origin point
# deg is degree for rotation
def rotate_vec(p1_,p2_,deg=0,c="blue"):
    #
    #   add your code
    #
    # comment out pass when implemented
    pass


# animates the two vector rotations
# long vector is represented by the points p1_ and p2_
# short vector is represented by the points p1_ and p3_
# p1_ is the origin point
# n is number of times the vectors are rotated 360 degrees
# c1 is the color for long vector
# c2 is the color for short vector
# note that this function contains the loop that calls rotate_vec
def animate_vec(p1_,p2_,p3_,c1,c2,n):
    #
    #   add your code
    #
    # comment out pass when implemented
    pass


if __name__ == "__main__":

    p1 = np.array([0,0])    # origin
    p2 = np.array([0,1])
    p3 = p2*.5

    init_plot()
    plot_vec(p1,p2,"blue")
    plot_vec(p1,p3,"red")

    # uncomment the following animate_vec function once implemented
    #animate_vec(p1,p2,p3,"blue","red",12)

    plt.show()