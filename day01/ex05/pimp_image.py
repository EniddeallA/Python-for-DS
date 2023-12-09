import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(ar):
    """
    This function inverts the colors of an image array
    and saves the inverted image.
    """
    new_arr = ar.copy()
    new_arr = 255 - new_arr
    plt.imshow(new_arr)
    plt.savefig("invert.png")
    return new_arr


def ft_red(ar):
    """
    This function applies a red filter to an image array
    and saves the filtered image.
    """
    new_arr = ar.copy()
    new_arr = new_arr * [1, 0, 0]
    plt.imshow(new_arr)
    plt.savefig("red.png")
    return new_arr[:, :, 0]


def ft_green(ar):
    """
    This function applies a green filter to an image array
    and saves the filtered image.
    """
    new_arr = ar.copy()
    new_arr = new_arr - [255, 0, 255]
    plt.imshow(new_arr)
    plt.savefig("green.png")
    return new_arr


def ft_blue(ar):
    """
    This function takes an image array, converts it to grayscale,
    and saves the grayscale image.
    """
    new_arr = ar.copy()
    new_arr[:, :, 0:2] = 0
    plt.imshow(new_arr)
    plt.savefig("blue.png")
    return new_arr


def ft_grey(array):
    """
    This function takes an image array, converts it to grayscale,
    and saves the grayscale image.
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = np.sum([red_channel, green_channel, blue_channel], axis=0)
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    plt.imshow(grey_image.astype(np.uint8))
    plt.savefig("grey.png")


def main():
    array = ft_load("fdf.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)


if __name__ == "__main__":
    main()
