import string
import sys


def text_analyzer(s=None):
    ''' This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text. '''
    if s is None:
        print("What is the text to count?")
        s = input(">>")
    if not isinstance(s, str):
        exit("AssertionError: argument is not a string")
    is_upper = 0
    is_lower = 0
    is_punc = 0
    is_space = 0
    is_digit = 0
    for c in s:
        if c.islower():
            is_lower += 1
        elif c.isupper():
            is_upper += 1
        elif c in string.punctuation:
            is_punc += 1
        elif c.isspace():
            is_space += 1
        elif c.isdigit():
            is_digit += 1
    print(f'The text contains {len(s)} character(s):')
    print(f'- {is_upper} upper letter(s)')
    print(f'- {is_lower} lower letter(s)')
    print(f'- {is_punc} punctuation mark(s)')
    print(f'- {is_space} space(s)')
    print(f'- {is_digit} digit(s)')


def main(s=None):
    text_analyzer(s)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        main()
    else:
        exit("AssertionError: more than one argument provided")
