import matplotlib.pyplot as plt
import matplotlib.image as img
from numpy import ndarray
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def ft_load(path: str) -> ndarray:
    try:
        image = img.imread(path)
    except FileNotFoundError:
        return f"File {path} not found"
    print(f"The shape of the image is: {image.shape}")
    print(image)
    return image

array = ft_load("landscape.jpeg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
