import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def ft_load(path):
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return f"File {path} not found"
    # print(f"The shape of the image is: {image.shape}")
    ar = np.array(image)
    print (ar)
    return ar

array = ft_load("/Users/akhalid/Desktop/Python-for-DS/day01/ex05/landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)