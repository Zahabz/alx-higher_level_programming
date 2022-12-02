#!/usr/bin/python3

if __name__ == '__main__':
    """Prints out the result of adding all command line arguments"""
    import sys

    arg_no = len(sys.argv) - 1
    result = 0
    for i in range(arg_no):
        result += int(sys.argv[i + 1])

    print(f'{result}')
