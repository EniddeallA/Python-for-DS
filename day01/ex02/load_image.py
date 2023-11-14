import numpy as np
from PIL import Image


def ft_load(path: str) -> str:
    try:
        img = Image.open(path, 'r')
    except FileNotFoundError:
        return f"File {path} not found"
    w, h = img.size
    pixel_values = list(img.getdata())
    shape = np.array(pixel_values).reshape((w, h, 3))
    print(pixel_values)
    return f"The shape of image is: {shape.shape}"


def main():
    ft_load("animal.jpeg")


if __name__ == "__main__":
    main()