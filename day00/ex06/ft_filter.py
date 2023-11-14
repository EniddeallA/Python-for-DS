def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


def ft_filter(function, iterable):
    for i in iterable:
        if function(i):
            yield i


def main():
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
    filtered = filter(fun, sequence)
    print(list(filtered))


if __name__ == "__main__":
    main()