import sys

def whatis(number):
    if not isinstance(number, int):
        raise AssertionError("argument is not an integer")
    
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
        r = whatis(number)
        print(r)
    except ValueError:
        print("AssertionError: argument is not an integer")
elif len(sys.argv) == 1:
    pass  # Do nothing if no arguments are provided
else:
    print("AssertionError: more than one argument is provided")