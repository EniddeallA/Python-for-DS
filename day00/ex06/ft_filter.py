def func(variable):
    """Function that takes a character and returns True if it is a vowel,
 False otherwise."""
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for i in iterable:
        if function(i):
            yield i


def main():
    original = filter.__doc__
    copy = ft_filter.__doc__
    print(copy)  # output: docstring
    print(original == copy)  # output: True
    # sequence1
    seq = [0, 1, 2, 3, 5, 8, 13]
    # result contains odd numbers of the list
    result = ft_filter(lambda x: x % 2 != 0, seq)
    print(list(result))
    # result contains even numbers of the list
    result = ft_filter(lambda x: x % 2 == 0, seq)
    print(list(result))

    # sequence2
    sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
    filtered = filter(func, sequence)
    print(list(filtered))


if __name__ == "__main__":
    main()
