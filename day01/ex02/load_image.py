import matplotlib.pyplot as plt


def ft_load(path):
    """
    This function loads an image from the given path
    and prints its shape and pixel values.
    """
    try:
        if path.split(".")[-1] == "jpg" or path.split(".")[-1] == "jpeg":
            image = plt.imread(path)
            print(f"The shape of the image is: {image.shape}")
            print(image)
            return image
        else:
            exit(f"File {path} is not a valid image file")
    except FileNotFoundError:
        exit(f"File {path} not found")


def main():
    ft_load("landscape.jpg")


if __name__ == "__main__":
    main()
