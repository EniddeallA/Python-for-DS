import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(path: str):
    """
    This function loads an image from the given path, slices it,
    and then displays and saves the sliced image.
    """
    image = ft_load(path)
    sliced_image = image[100:500, 450:850, :3]
    print(f"The new shape of the image after slicing is: {sliced_image.shape}")
    print(sliced_image)
    plt.imshow(sliced_image)
    plt.savefig("sliced_image.png")
    plt.show()


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
