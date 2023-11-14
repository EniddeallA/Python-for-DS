import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def rotate(path: str):
    image = img.imread(path)
    print(f"The shape of the image is: {image.shape}")
    print(image)
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