class calculator:
    def __init__(self, v1: list[float], v2: list[float]) -> None:
        self.v1 = v1
        self.v2 = v2

    def dotproduct(V1: list[float], V2: list[float]):
        if (len(V1) != len(V2)):
            exit("ERROR (dotproduct)")
        else:
            dp = 0
            for i in range(len(V1)):
                dp += V1[i] * V2[i]
            print("Dot product is: ", dp)

    def add_vec(V1: list[float], V2: list[float]):
        if (len(V1) != len(V2)):
            exit("ERROR (add_vec)")
        else:
            S = []
            for i in range(len(V1)):
                S.append(float(V1[i] + V2[i]))
            print("Add Vector is: ", S)

    def sous_vec(V1: list[float], V2: list[float]):
        if (len(V1) != len(V2)):
            exit("ERROR (sous_vec)")
        else:
            S = []
            for i in range(len(V1)):
                S.append(float(V1[i] - V2[i]))
            print("Sous Vector is: ", S)


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
