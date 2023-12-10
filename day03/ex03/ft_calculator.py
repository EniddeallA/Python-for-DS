class calculator:
    def __init__(self, n: list[int | float]) -> None:
        self.n = n

    def __add__(self, object) -> None:
        for i in range(len(self.n)):
            self.n[i] += object
        print(self.n)

    def __mul__(self, object) -> None:
        for i in range(len(self.n)):
            self.n[i] *= object
        print(self.n)

    def __sub__(self, object) -> None:
        for i in range(len(self.n)):
            self.n[i] -= object
        print(self.n)

    def __truediv__(self, object) -> None:
        if (object == 0):
            exit("ERROR (div by zero)")
        for i in range(len(self.n)):
            self.n[i] /= object
        print(self.n)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
