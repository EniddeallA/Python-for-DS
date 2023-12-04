import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
import matplotlib.image as img

def ft_invert(ar):
    new_arr = ar.copy()
    new_arr = 255 - new_arr
    plt.imshow(new_arr)
    plt.savefig("invert.png")
    #plt.show()
    return new_arr


def ft_red(ar):
    new_arr = ar.copy()
    new_arr = new_arr * [1, 0, 0]
    plt.imshow(new_arr)
    plt.savefig("red.png")
    #plt.show()
    return new_arr[:, :, 0]


def ft_green(ar):
    new_arr = ar.copy()
    new_arr = new_arr - [255, 0, 255]
    plt.imshow(new_arr)
    plt.savefig("green.png")
    #plt.show()
    return new_arr


def ft_blue(ar):
    new_arr = ar.copy()
    new_arr[:, :, 0:2] = 0
    plt.imshow(new_arr)
    plt.savefig("blue.png")
    #plt.show()
    return new_arr


def ft_grey(ar):
    new_arr = ar.copy()
    new_arr[:, :, 0:3] = np.sum([new_arr[:, :, 0:1] * 0.299, 0.587 * new_arr[:, :, 1:2], 
                            0.114 * new_arr[:, :, 2:3]], axis=0)
    plt.imshow(new_arr)
    plt.savefig("grey.png")
    #plt.show()
    return new_arr 


