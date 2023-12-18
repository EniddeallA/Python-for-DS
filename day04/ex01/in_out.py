def square(x: int | float) -> int | float:
    """Returns the square of a number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the power of a number."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that applies the function passed as parameter"""
    count = x

    def inner() -> float:
        """Returns the result of the function passed as parameter"""
        nonlocal count
        count = function(count)
        return count
    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
