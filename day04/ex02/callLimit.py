def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} called more than {limit} times")
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(4):
        f()
        g()


if __name__ == "__main__":
    main()
