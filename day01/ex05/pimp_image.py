import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
import matplotlib.image as img

def ft_invert(array: ndarray) -> ndarray:
    ar = np.array(array)
    plt.imshow(1 - ar)
    plt.savefig("invert.png")
    plt.show()
    return 1 - array


def ft_red(array: ndarray) -> ndarray:
    plt.imshow(array[:, :, 0])
    plt.savefig("red.png")
    plt.show()
    return array[:, :, 0]


def ft_green(array: ndarray) -> ndarray:
    plt.imshow(array[:, :, 1])
    plt.savefig("green.png")
    plt.show()
    return array[:, :, 1]


def ft_blue(array: ndarray) -> ndarray:
    plt.imshow(array[:, :, 2])
    plt.savefig("blue.png")
    plt.show()
    return array[:, :, 2]


def ft_grey(array: ndarray) -> ndarray:
    plt.imshow(array[:, :, 0] * 0.299 + array[:, :, 1] * 0.587 + array[:, :, 2] * 0.114)
    plt.savefig("grey.png")
    plt.show()
    return array[:, :, 0] * 0.299 + array[:, :, 1] * 0.587 + array[:, :, 2] * 0.114