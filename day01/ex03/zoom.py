import matplotlib.pyplot as plt
import matplotlib.image as img


def zoom(path: str):
    image = img.imread(path)
    print(f"The shape of the image is: {image.shape}")
    print(image)
    sliced_image = image[100:500, 450:850, :3]
    print(f"The new shape of the image after slicing is: {sliced_image.shape}")
    plt.imshow(sliced_image)
    plt.savefig("sliced_image.png")
    plt.show()


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()