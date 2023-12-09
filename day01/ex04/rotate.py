import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def rotate(path: str):
    """
    This function loads an image from the given path,
    slices it, transposes it, and then displays and
    saves the transposed image.

    Parameters:
    path (str): The path of the image file.
    """
    image = ft_load(path)
    s = image[100:500, 450:850, :3]
    transpose = [[s[j][i] for j in range(len(s))] for i in range(len(s[0]))]
    transpose = np.array(transpose)
    plt.imshow(transpose)
    print(f"The new shape of the image after transpose is: {transpose.shape}")
    print(transpose)
    plt.savefig("sliced_image.png")
    plt.show()


def main():
    rotate("animal.jpeg")


if __name__ == "__main__":
    main()
