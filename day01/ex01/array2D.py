def slice_me(family: list, start: int, end: int) -> list:
    """
    This function slices a 2D list (matrix) from the given
    start index to the end index.

    Parameters:
    family (list): A 2D list (matrix) to be sliced.
    start (int): The start index for slicing.
    end (int): The end index for slicing.

    Returns:
    list: A sliced 2D list (matrix).
    """
    for i in family:
        if type(i) is not list:
            exit("Error: Not a list.")
        if len(i) != len(family[0]):
            exit("Error: Not a matrix.")
    print(f"My shape is ({len(family), len(family[0])})")
    print(f"""My new shape is ({len(family[start:end]),
          len(family[start:end][0])})""")
    return family[start:end]
