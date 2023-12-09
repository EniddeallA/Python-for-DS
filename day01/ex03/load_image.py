import matplotlib.pyplot as plt


def ft_load(path):
    """
    This function loads an image from the given path
    and prints its pixel values.
    It also returns the shape of the image.
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
