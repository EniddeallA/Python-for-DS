def slice_me(family: list, start: int, end: int) -> list:
    """
    This function slices a 2D list (matrix) from the given
    start index to the end index.
    """
    for i in family:
        if type(i) is not list:
            exit("Error: Not a list.")
        if len(i) != len(family[0]):
            exit("Error: Not a matrix.")
    print(f"My shape is {len(family), len(family[0])}")
    print(f"""My new shape is {len(family[start:end]),
          len(family[start:end][0])}""")
    return family[start:end]


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
