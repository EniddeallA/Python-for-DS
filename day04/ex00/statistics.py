def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the mean, median, quartile, standard deviation
    and variance of a list of numbers."""
    for kwarg in kwargs.items():
        if kwarg[1] == "mean":
            if not args:
                print("ERROR")
            else:
                print("mean:", sum(args) / len(args))
        elif kwarg[1] == "median":
            if not args:
                print("ERROR")
            else:
                print("median:", sorted(args)[len(args) // 2])
        elif kwarg[1] == "quartile":
            if not args:
                print("ERROR")
            else:
                print("quartile", [float(sorted(args)[len(args) // 4]),
                                   float(sorted(args)[len(args) // 4 * 3])])
        elif kwarg[1] == "std":
            if not args:
                print("ERROR")
            else:
                print("std:", (sum([(x - sum(args) / len(args)) ** 2
                                    for x in args]) / len(args)) ** 0.5)
        elif kwarg[1] == "var":
            if not args:
                print("ERROR")
            else:
                print("var:", sum([(x - sum(args) / len(args)) ** 2
                                   for x in args]) / len(args))


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                  world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
